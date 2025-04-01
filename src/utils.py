```python
from chains import travel_chain, tips_chain

def get_travel_recommendations(source, destination):
    return travel_chain.run(source=source, destination=destination)

def get_travel_tips(destination):
    return tips_chain.run(destination=destination)
```
