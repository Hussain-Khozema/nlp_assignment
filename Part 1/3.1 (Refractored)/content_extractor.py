import os
import config

def extract_content(domain):
    all_data = []
    all_files = config.getFilesInDirectory(domain,config.FOLDERS['DATA_FOLDER'])
    for file_name in all_files:
        file_url = config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS["DATA_FOLDER"] + file_name
        with open(file_url, 'r', encoding="utf-8") as f:
            text =  f.read().encode('utf-8')
            filt_text = text.decode("utf-8").replace('\n','').replace('\xad', '')
            all_data.append({'file_name': file_name, 'text': filt_text})
        f.close()

    return all_data
