import yadisk
import os
import zipfile


def initialization():

    def line_extract(line: str, target_value):

        sym_number = line.find('=')
        if target_value == line[:sym_number]:
            return line[sym_number + 1:]
        else:
            return None

    global FOLDER, disk
    CONFIG_FILE = './config.txt'
    print('Config initialization...')

    try:
        file = open(CONFIG_FILE, 'r')
        TOKEN = str(line_extract(file.readline().rstrip('\n'), 'token'))
        FOLDER = str(line_extract(file.readline(), 'folder'))

    except:
        print('Config reading error')
        return False

    finally:
        print(f'Token: ...{(TOKEN[40:])}')
        print(f'Directory: {FOLDER}')
        file.close()

    try:
        disk = yadisk.YaDisk(token=TOKEN)
        t = disk.check_token()
        print('Token:', t)

    except:
        print('Token error')
        return False

    finally:

        if not disk.exists(FOLDER):
            disk.mkdir(FOLDER)

        return disk.check_token()


def listdisk():

    dlist = []
    print('Files on yadisk:')
    n = 0
    for i in disk.listdir(FOLDER):
        print(f'{n}) {i.name}')
        dlist.append(i.name)
        n += 1

    return dlist


def upload():

    path = input('Path of file or directory to upload: ')
    name = input('Enter the name of file on yadisk: ')

    if os.path.isfile(path):
        try:
            with zipfile.ZipFile(f'{name}.zip', 'w') as zfile:
                zfile.write(path)
            disk.upload(f'./{name}.zip', f'{FOLDER}/{name}')
            print(f'{path} uploaded to yadisk as {name}')

        except:
            print('Unable to upload')
        finally:
            os.remove(f'./{name}.zip')

    elif os.path.isdir(path):

        try:
            with zipfile.ZipFile(f'{name}.zip', 'w') as zfile:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        zfile.write(os.path.join(root, file))

            disk.upload(f'./{name}.zip', f'{FOLDER}/{name}.zip')
            print(f'{path} uploaded in yadisk as {name}.zip')

        except:
            print('Unable to upload')
        finally:
            os.remove(f'./{name}.zip')


def download():

    if not os.path.exists('./downloads'):
        os.mkdir('./downloads')

    dlist = listdisk()
    n = int(input('File to download: '))
    path = input('Download to: ')
    name = input('Name of new file: ')
    try:
        if not path:
            path = f'./downloads'
        dfile = dlist[n]
        ext_n = dfile.find('.')
        ext = dfile[ext_n:]
        disk.download(f'{FOLDER}/{dfile}', f'{path}/{name}{ext}')
        print(f'Downloaded: {FOLDER}/{dfile} as {path}/{name}{ext}')

    except:
        print('Unable to download')


def remove():

    rlist = listdisk()
    n = int(input('File to remove: '))
    try:
        rfile = rlist[n]

        disk.remove(f'{FOLDER}/{rfile}')
        print(f'Removed: {FOLDER}/{rfile}')

    except:
        print('Unable to remove')


def main():

    if initialization():

        while True:

            print('Select action:')
            print('lst - show files on yadisk')
            print('upl - zip and upload')
            print('dwl - download')
            print('rem - remove file from yadisk')
            print('ext - stop and exit')
            act = input('>>>: ')

            if act == 'lst':
                listdisk()

            elif act == 'upl':
                upload()

            elif act == 'dwl':
                download()

            elif act == 'rem':
                remove()

            elif act == 'ext':
                break

            else:
                print('Incorrect input')
                continue

    else:
        print('Initialization error')
        return
    input('Enter to exit...')


if __name__ == '__main__':
    main()
