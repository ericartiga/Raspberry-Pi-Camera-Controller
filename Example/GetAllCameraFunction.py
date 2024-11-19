import gphoto2 as gp

def print_camera_config(camera):
    config = camera.get_config()
    # Function to recursively print the configuration tree
    def print_config(child, depth=0):
        indent = "  " * depth
        print(f"{indent}- {child.get_name()}: {child.get_type()}")
        for i in range(child.count_children()):
            print_config(child.get_child(i), depth + 1)
    
    print_config(config)

if __name__ == "__main__":
    try:
        camera = gp.Camera()
        camera.init()
        print_camera_config(camera)  # Print the camera configuration
        camera.exit()
    except Exception as e:
        print("An error occurred:", str(e))
