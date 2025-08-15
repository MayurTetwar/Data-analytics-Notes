# python -u "e:\Python\Project\Youtube_maneger.py"

import json

def load_Data():
    try:
        with open("Youtube.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("Youtube.txt",'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('\n')
    print('*'*70)
    for index,video in enumerate(videos,start=1):
        print(f'{index}. Name: {video['name']}, Duration: {video['time']}')
    print('*'*70)

def add_video(videos):
    name=input("Enter video name:- ")
    time=input("Enter video time:- ")
    videos.append({"name":name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    update_no=int(input("Enter the video number to update:-"))
    if(1<=update_no<=len(videos)):
        name=input("Enter new video name:- ")
        time=input("Enter new video time:- ")
        videos[update_no-1]={"name":name,"time":time}
        save_data_helper(videos)
    else:
        print("Invalid index selction.....")

def delete_video(videos):
    list_all_videos(videos)
    del_no=int(input("Enter the video number to delete:- "))
    if(1<=del_no<=len(videos)):
        del videos[del_no-1]
        save_data_helper(videos)
    else:
        print("Invalid index selctions.....")


def main():
    videos=load_Data()
    while(True):
        print("Youtube Maneger:- (choice Input) ")
        print("1. List all youtube vidoes ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video Details")
        print("4. Delete a youtube video ")
        print("5. Exit")
        choice=input("Enter your choice:- ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice....")


if(__name__=="__main__"):
    main()
