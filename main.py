import argparse

def main():
    parser = argparse.ArgumentParser(
                        prog='expense-tracker',
                        description='It helps you to manage your monthly expenses')
    subparser = parser.add_subparsers(dest="command")

    # expense-tracker add 
    parser_add = subparser.add_parser("add")
    parser_add.add_argument("--description" , required=True)
    parser_add.add_argument("--amount" , type = float , required=True)

    # expense-tracker list
    parser_list = subparser.add_parser("list")

    # expense-tracker summary and --month <int>
    parser_summary = subparser.add_parser("summary")
    parser_summary.add_argument("--month" , type = int ,  required=False)

    # expense-tracker delete --id <int>
    parser_delete = subparser.add_parser("delete")
    parser_delete.add_argument("--id" , type=int , required=True)
    
 
    # Parse and Route
    args = parser.parse_args()

    if args.command=='add':
        print(args.description , args.amount)
    elif args.command=="list":
        print("Print is working!")
    elif args.command=="summary":
        if args.month:
            print("This is a specific summary!")
            print(args.month)
        print("Summary is working!")
    elif args.command=="delete":
        print("delet %s" % args.id)
    else:           
        parser.print_help()

if __name__ == "__main__":
    main()