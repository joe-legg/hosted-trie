import requests
import argparse as arg
import sys

SERVER_URL = "http://127.0.0.1:8000"

def insert(args):
    try:
        requests.post(f"{SERVER_URL}/trie/{args.keyword}")
    except:
        print("error inserting keyword")

def delete(args):
    try:
        requests.delete(f"{SERVER_URL}/trie/{args.keyword}")
    except:
        print("error deleting keyword")

def search(args):
    try:
        req = requests.get(f"{SERVER_URL}/trie/{args.keyword}")
        keywords = req.json()["keywords"]

        if len(keywords) == 1 and keywords[0] == args.keyword:
            print("true")
        else:
            print("false")
    except:
        print("error searching for keyword")

def suggest(args):
    try:
        req = requests.get(f"{SERVER_URL}/trie/{args.prefix}")
        keywords = req.json()["keywords"]

        for word in keywords:
            print(word)
    except:
        print("error getting suggestions from the trie")

def list(args):
    try:
        req = requests.get(f"{SERVER_URL}/trie")
        keywords = req.json()["keywords"]

        for word in keywords:
            print(word)
    except:
        print("error getting list of keywords")

if __name__ == "__main__":
    arg_parser = arg.ArgumentParser(description="CLI for trie")
    sub_parsers = arg_parser.add_subparsers()

    p_insert = sub_parsers.add_parser("insert", help="insert a keyword into the trie")
    p_insert.add_argument("keyword", type=str, help="the keyword to insert")
    p_insert.set_defaults(func=insert)

    p_delete = sub_parsers.add_parser("delete", help="delete a keyword from the trie")
    p_delete.add_argument("keyword", type=str, help="the keyword to delete")
    p_delete.set_defaults(func=delete)

    p_search = sub_parsers.add_parser("search", help="check if a keyword exists in the trie")
    p_search.add_argument("keyword", type=str, help="the keyword to search for")
    p_search.set_defaults(func=search)

    p_suggest = sub_parsers.add_parser("suggest", help="get autocomplete suggestions for a prefix")
    p_suggest.add_argument("prefix", type=str, help="the prefix to get suggestions for")
    p_suggest.set_defaults(func=suggest)

    p_list = sub_parsers.add_parser("list", help="get a list of all the words in the trie")
    p_list.set_defaults(func=list)

    if not len(sys.argv) > 1:
        arg_parser.parse_args(["--help"])
        sys.exit(0)

    args = arg_parser.parse_args()
    args.func(args)
