
import time
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.database import DatabaseInstance
from databricks.sdk.errors import NotFound


"""
In this example, we're using the Databricks Workspace client to manage database instances.
To use this script, you need to:

1. Configure the Databricks CLI with your workspace credentials:
   - Install the Databricks CLI: `pip install databricks-cli`
   - Configure credentials: `databricks configure --profile <profile-name>`
   - Enter your workspace URL and personal access token when prompted

2. Update the PROFILE variable below to match your configured profile name

For more information on configuring the Databricks CLI, see:
https://docs.databricks.com/dev-tools/cli/index.html
"""

INSTANCE_NAME = "rb-demo-lakebase"
PROFILE = "az-demo"
CAPACITY = "CU_1"


# Initialize the Workspace client
w = WorkspaceClient(profile=PROFILE)


def print_instance_details(instance):
    """Print details of a database instance"""
    print(f"Instance Name: {instance.name}")
    print(f"Capacity: {instance.capacity or 'Not specified'}")
    print(f"State: {instance.state or 'Unknown'}")
    print(f"Creation Time: {instance.creation_time or 'Not available'}")
    print(f"Creator: {instance.creator or 'Not available'}")
    print(f"PostgreSQL Version: {instance.pg_version or 'Not available'}")
    print(f"Stopped: {instance.effective_stopped or False}")
    
    # DNS endpoints might not be immediately available
    if instance.read_write_dns:
        print(f"Read/Write DNS: {instance.read_write_dns}")
    else:
        print("Read/Write DNS: Not yet available (instance may still be provisioning)")
    
    if instance.read_only_dns:
        print(f"Read-Only DNS: {instance.read_only_dns}")
    elif instance.effective_enable_readable_secondaries:
        print("Read-Only DNS: Not yet available (instance may still be provisioning)")
    else:
        print("Read-Only DNS: Not configured (readable secondaries disabled)")

def wait_for_instance_ready(instance_name, timeout_minutes=20):
    """
    Wait for database instance to be fully provisioned and ready for use.
    
    Args:
        instance_name: Name of the database instance
        timeout_minutes: Maximum time to wait (default: 20 minutes)
    
    Returns:
        DatabaseInstance: The fully provisioned instance
        
    Raises:
        TimeoutError: If instance isn't ready within the timeout period
    """
    print(f"\n⏳ Waiting for instance '{instance_name}' to be fully provisioned...")
    print("   This typically takes 5-15 minutes for database instances.")
    
    start_time = time.time()
    timeout_seconds = timeout_minutes * 60
    poll_interval = 30  # Check every 30 seconds
    
    while time.time() - start_time < timeout_seconds:
        try:
            instance = w.database.get_database_instance(instance_name)
            
            # Check if instance state is AVAILABLE (fully ready for connections)
            state_str = str(instance.state) if instance.state else 'Unknown'
            
            if instance.state and ('AVAILABLE' in state_str or 'ONLINE' in state_str):
                elapsed_minutes = (time.time() - start_time) / 60
                print(f"✅ Instance is ready! (took {elapsed_minutes:.1f} minutes)")
                print(f"   Final State: {state_str}")
                return instance
            
            # Show current state for debugging
            elapsed_seconds = int(time.time() - start_time)
            print(f"   [{elapsed_seconds}s] State: {state_str} - Still provisioning...")
            
            time.sleep(poll_interval)
            
        except Exception as e:
            print(f"   ⚠️  Error checking instance status: {e}")
            time.sleep(poll_interval)
    
    # Timeout reached
    elapsed_minutes = timeout_minutes
    raise TimeoutError(f"❌ Instance '{instance_name}' was not ready after {elapsed_minutes} minutes. "
                      f"Check Databricks console for status updates.")

# Check if instance already exists
try:
    existing_instance = w.database.get_database_instance(INSTANCE_NAME)
    print(f"Database instance '{INSTANCE_NAME}' already exists!")
    print("\nInstance Details:")
    print_instance_details(existing_instance)
    
except NotFound:
    print(f"Database instance '{INSTANCE_NAME}' does not exist. Creating new instance...")
    
    # Create a database instance (this returns immediately, doesn't wait for completion)
    instance = w.database.create_database_instance(
        DatabaseInstance(
            name=INSTANCE_NAME,
            capacity=CAPACITY
        )
    )
    
    print(f"✅ Database instance creation initiated: {instance.name}")
    print("🔄 This is an asynchronous operation - the instance is now being provisioned...")
    
    try:
        # Wait for the instance to be fully ready
        ready_instance = wait_for_instance_ready(INSTANCE_NAME)
        
        print("\n📋 Final Instance Details:")
        print_instance_details(ready_instance)
        
    except TimeoutError as e:
        print(f"\n{e}")
        print("\n📋 Current Instance Status (may still be provisioning):")
        current_instance = w.database.get_database_instance(INSTANCE_NAME)
        print_instance_details(current_instance)

except Exception as e:
    print(f"❌ Error checking/creating database instance: {e}")

