from interests.models import Interests
from django_pandas.io import read_frame

def top_interests():
    all_interests = Interests.objects.all()

    interests_df = read_frame(all_connections)

    interests_df.dropna(inplace = True)

    # converting to dic
    interests_dict = interests_df.to_dict()
    interest_names = data_dict['name'].values()
    interests = {}
    arr=[]
    for i in interest_names:
        arr.append(i)

    for i in arr:
        item = arr.count(i)
        interests[i] = item

    sorted_interests = sorted(interests.items(), key = lambda kv:(kv[1], kv[0]))
    return sorted_interests

print(top_interests())
