from typing import List
import tarfile
import os.path

def archive(name: str, in_dir: str, files: List[str]):
    archive_filename = f"{name}.tar.gz"
    archive_path = os.path.join(in_dir, archive_filename)
    tf = tarfile.open(archive_path, 'w:gz')

    for f in files:
        tf.add(f)

    tf.close()
