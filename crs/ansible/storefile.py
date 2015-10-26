# @Date    : 2015-10-26 00:11:30
# @Author  : miaolian (mike19890421@163.com)
# @Version : 1.0

import os

def ensure_dir(path,filepath = None):
	try:
		dir_path = get_real_dir(path)
		if filepath:
			dir_path = os.path.join(dir_path,filepath)
		if not os.path.exists(dir_path):
			os.makedirs(dir_path,mode=0755)
		return 0
	except:
		return -1

def get_real_dir(path):
	return os.path.realpath(path)

def get_project_dir(project_name):
    return get_real_dir(os.path.join(settings.ANSIBLE_PROJECTS_ROOT, project_name))

def ensure_project_dir(project_name):
	dir_proj = get_project_dir(project_name)
	if (ensure_dir(dir_proj)):
		return -1
	if(ensure_dir(dir_proj,"inventories")):
		return -1
	if(ensure_dir(dir_proj,"playbooks")):
		return -1
	if(ensure_dir(dir_proj,"vars")):
		return -1
	if(ensure_dir(dir_proj,"packages")):
		return -1
	if(ensure_dir(dir_proj,"data")):
		return -1
	return 0
