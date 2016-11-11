import os
def setup():
    '''
    initializing project variables
    '''
    lib_path = os.getcwd()+"/"

    temp_path = os.getcwd().split('/')[:-1]
    config_file_path = "/".join(temp_path)+"/config/"

    temp_path = os.getcwd().split('/')[:-1]
    project_path = "/".join(temp_path)+"/"

    print config_file_path
    print lib_path
    os.environ["config_files"] = config_file_path
    print project_path



setup()
