import A6000_Control

print('Please connect and switch on your camera')

while True:
    try:
        # Initialize the camera
        camera = gp.Camera()
        camera.init()
    except gp.GPhoto2Error as ex:
        if ex.code == gp.GP_ERROR_MODEL_NOT_FOUND:
            # No camera detected, try again in 2 seconds
            print("Camera not found. Retrying in 2 seconds...")
            time.sleep(2)
            continue
        # Raise any other errors that we can't handle
        raise
    # Operation completed successfully, exit loop
    print("Camera initialized successfully.")
    break

