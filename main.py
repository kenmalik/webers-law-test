from generators import set1, set2
from generators import set1_alt
from generators import graph1
from generators import graph1newset
from generators.sample import make_viz

def main():
    print("Weber's law test")
    make_viz()          # sample.py    (..)
    set1.make_viz()     # set1.py      (6 images, V1-V6)
    set1_alt.make_viz() # set1_alt.py  (3 images, set1_)
    set2.make_viz()
    graph1.make_viz()
    graph1newset.make_viz()

if __name__ == "__main__":
    main()
