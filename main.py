import argparse
import json
import os
from datetime import datetime 
#the data stucture
'''
{
    "id"int,
    "date":date,
    "description":text
    "amount":float
}
'''
#functions

def get_id():
    if not os.path.exists("data.json"):
        return 1
    try: 
        with open("data.json" , 'r') as f:
            content = f.read()
            if not content:
                return 1
            
            data = json.loads(content)

            if not data:
                return 1
            
            last_id = -1
            for expense in data:
                last_id = max(last_id , expense["id"])

            return last_id + 1
    except (json.JSONDecodeError , KeyError):
        return 1
    

def add(description , amount):

    id = get_id()

    if id == 1:
        data = []
    else:
        with open("data.json" , 'r') as f:
            data = json.load(f)

    new_expense = {
        "id":id,
        "date":datetime.now().strftime("%Y-%m-%d %H:%M"),
        "description":description,
        "amount":amount
    }

    data.append(new_expense)

    with open("data.json" , 'w') as f:
        json.dump(data , f , indent=4)
    print(f"Expense added successfully (ID: {id})")
    

def list():
    pass
def summary(month=None):
    pass
def delete(id):
    pass



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
        add(args.description , args.amount)
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