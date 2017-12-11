#get all liked page
import facebook
import io
import json

def saved_to_file(file_name, data):
    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
    print("Success in saved ",file_name)

def get_liked_pages(user_token = ""):
    try:
        graph = facebook.GraphAPI(access_token = user_token,version = "2.7")
        user_id = graph.get_object(id = "me?fields=likes")["id"]
        #obj = graph.get_object(id = "me?fields=likes")
        obj = graph.get_object("100005064335645/likes?pretty=1&limit=100")
        #obj = obj["likes"]
        liked_pages = list()
        request = str()
        while obj["paging"]["cursors"]["after"] is not "":
            liked_pages.extend(obj["data"])
            _next = obj["paging"]["cursors"]["after"]
            request =user_id + "/likes?pretty=1&limit=100&after=" + _next;
            obj = graph.get_object(request,version = "2.7")
    except Exception as error:
        print("Detail: ",error)
        saved_to_file("list_pages.txt",liked_pages)
        saved_to_file("obj.txt",obj)
        print(len(liked_pages))
        print(request)

def main():
    my_token = "EAACEdEose0cBAF08pvIg88BDaV97cGZAyniCyTXh5kL1B7hX9LOWVzUBC1wW8KTkZBY1M3wV6GKROWFQoI8TbFVEBgiIKGRod6UV2ZBhZBq3qFvZAZAqLnM9nZC45WZAPLb47P55xinNarOVLF3eGQnKDdCzPCJ9nOnQHUA8pxUdE0H771IpDWYZCkCy2C4BNEhIZD"
    get_liked_pages(my_token)

if __name__ == "__main__":
    main()
