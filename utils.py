import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-t", "--test", help="Test")
    arg_parser.add_argument("-tf", "--test-file", help="Test file")
    arg_parser.add_argument("-s", "--sentesces", help="Sentesces")
    config = arg_parser.parse_args()

    if config.test:
        print('[{}]'.format(config.test.replace(' ', ',')))

    if config.test_file:
        f = open(config.test_file)
        for line in f:
            if (not line[0] == '%') and (line.strip()):
                strip_line = line.split(']')[0]
                print ('rec' + strip_line.strip()[10:] + '].\n')

    if config.sentesces:
        f = open(config.sentesces)
        for line in f:
            if (not line[0] == '%') and (line.strip()):
                true_false = ']).'
                if line[0] == '*':
                    true_false = '],fails).'
                sentesce = 'test_sent(['
                for s in line.strip().replace('*', '').split():
                    sentesce += s + ','
                print(sentesce[:-1]+true_false)
            else:
                print line.strip()
if __name__ == '__main__':
    main()