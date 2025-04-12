import sys
import random
from extract_words import NMS_FILE, NFS_FILE, NMP_FILE, NFP_FILE, AMS_FILE, AFS_FILE, AMP_FILE, AFP_FILE
import os

nms_file = open(NMS_FILE, 'r')
nms_lines = nms_file.readlines()
nms_file.close()
nfs_file = open(NFS_FILE, 'r')
nfs_lines = nfs_file.readlines()
nfs_file.close()
nmp_file = open(NMP_FILE, 'r')
nmp_lines = nmp_file.readlines()
nmp_file.close()
nfp_file = open(NFP_FILE, 'r')
nfp_lines = nfp_file.readlines()
nfp_file.close()
ams_file = open(AMS_FILE, 'r')
ams_lines = ams_file.readlines()
ams_file.close()
afs_file = open(AFS_FILE, 'r')
afs_lines = afs_file.readlines()
afs_file.close()
amp_file = open(AMP_FILE, 'r')
amp_lines = amp_file.readlines()
amp_file.close()
afp_file = open(AFP_FILE, 'r')
afp_lines = afp_file.readlines()
afp_file.close()


for i in range(100):
    # print(f"{random.choice(nfp_lines).strip()}{random.choice(afp_lines).strip()}")
    # print(f"{random.choice(nfs_lines).strip()}{random.choice(ams_lines).strip()}")
    # print(f"{random.choice(nmp_lines).strip()}{random.choice(amp_lines).strip()}")
    # print(f"{random.choice(nms_lines).strip()}{random.choice(ams_lines).strip()}")
    nombre = ""
    if random.choice([True, False]):
        nombre = f"{random.choice(nms_lines).strip()}{random.choice(ams_lines).strip()}"
    elif random.choice([True, False]):
        nombre = f"{random.choice(nmp_lines).strip()}{random.choice(amp_lines).strip()}"
    elif random.choice([True, False]):
        nombre = f"{random.choice(nfs_lines).strip()}{random.choice(afs_lines).strip()}"
    else:
        nombre = f"{random.choice(nfp_lines).strip()}{random.choice(afp_lines).strip()}"
    
    extra = ""

    if random.choice([True, False]):
        extra = f"del {random.choice(nms_lines).strip()}"
    elif random.choice([True, False]):
        extra = f"de la {random.choice(nfs_lines).strip()}"
    elif random.choice([True, False]):
        extra = f"de los {random.choice(nmp_lines).strip()}"
    else:
        extra = f"de las {random.choice(nfp_lines).strip()}"
    print(f"{nombre.capitalize()} {extra.lower()}")
    