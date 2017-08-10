# demonstrates four different types of args and their uses.
# untested

import shutil, os.path

def augmented_move(target_folder, *filenames, verbos = False, **specific):
    '''Moves all filenames into the target folder, allowing specific treatment
    of certain files'''

    def print_verbose(message, filename):
        '''print message only if verbose is enabled'''
        if verbose:
            print(message.format(filenmae))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific{filename] == 'ignore':
                print_verbose('Ignoring {0}', filename)
            elif specific[filename] == 'copy':
                print_verbose('Copying {0}', filename)
                shutil.copyfile(filename, target_path)
            else:
                print_verbose('Moving {0}', filename)
                shutil.move(filename, target_path)
        
                

