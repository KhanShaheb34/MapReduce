# MapReduce
Learning Hadoop MapReduce

## Let's see an WordCount example

### Step 1:
Install docker

### Step 2: Start Hadoop
Follow [this tutorial](https://shortcut.com/developer-how-to/how-to-set-up-a-hadoop-cluster-in-docker) to start a hadoop cluster using docker.

> Use `docker-compose.yml` file from the gist.

### Step 3: Install python in the nodes
Open terminal in each node of the hadoop cluster and install python3 in it.

- To open bash in a cluster: `docker exec -it namenode bash` (change `namenode` to whichever node you want to open)
- To install python3: `apt update && apt upgrade && apt install python3`

> To check the name of the nodes: `docker ps` or open Docker Desktop on windows/mac

> Enough tel hole ami `docker-compose.yml` file ta edit kore dibo, taile ar koshto kore ei step kora lagbe na.

### Step 4: Create `mapper.py`
Currently I'm just sharing the codes, again, enough tel hole describe korbo pore. Plus, python easy, code porlei bujha jay, ki hocche...

```python
#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(word + "\t1")
```

### Step 5: Create `reducer.py`

```python
#!/usr/bin/python3
# -*-coding:utf-8 -*

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(current_word + "\t" + str(current_count))
        current_count = count
        current_word = word

if current_word == word:
    print(current_word + "\t" + str(current_count))
```

### Step 6: Testing locally
To test it locally you can create a text file with ja khushi ta inside it and run:

```sh
cat input.txt | mapper.py | sort -k1,1 | reducer.py
```

> Mood ashle pore shob explain korbo

### Step 7: Copy files to namenode

Copy your input.txt, mapper.py and reducer.py to hadoop namenode:

```sh
docker cp input.txt eff4f966c9ef:MapReduceTut/input.txt
docker cp mapper.py eff4f966c9ef:MapReduceTut/mapper.py
docker cp reducer.py eff4f966c9ef:MapReduceTut/reducer.py

# Write your namenode hash instead of eff4f966c9ef
# And I created a folder called MapReduceTut in hadoop to organize things easily, so I'm copying to that folder.
```

### Step 8: Let's go too hadooooooop
At first open terminal in the hadoop namenode: `docker exec -it namenode bash`

Then put your input file on hdfs in a new folder:

```sh
hdfs dfs -mkdir input
hdfs dfs -put input.txt input/input.txt

# Why new folder? Idk!
```

### Step 9: Time to run MapReduce

Just run:

```sh
mapred streaming \
-input input/input.txt \
-output output \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-file /MapReduceTut/mapper.py \
-file /MapReduceTut/reducer.py
```

> Insha'Allah pore eita o explain korbo

### Step 10: Pray
Vai, dua kor, oju kore namaj pore ay, time lagbe ager step e onek... Allah rohom na korle fail korbe!

### Step 11: Output
Allahr rohomot e kaj hoye gele output dekhar jonno: `hdfs dfs -cat otput/*`
