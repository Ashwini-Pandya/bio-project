print("Welcome to ANIMAL KINGDOM")

print('Why are we so curious to know about animals ?')

print('''When you look around, you will observe different animals with different structures and forms.
As over a million species of animals have described till now, the need for classification  becomes all the more important.
The classification also helps in assigning systematic position to newly described species.''')

print("What you want to go for?")
def menu1():
    print(''' 
    1.Basis Of classification
    2.Classification of Animals
    ''')
    print("Note: If you do'nt know the basics of classification please go for the option 1.")
    return int(input("Select anyoption from above given menu."))

# Aashika's functions
def basicmenu():
        print("""BASIS OF CLASSIFICATION
        INTRODUCTION:
        Inspite of differences in structures and form of different animals,
        there are fundamental features common to various individuals in
        relation to the arrangement of cells,body symmetry,nature of coelom,
        pattern of digesive,circulatory or reproductive systems.These features
        are used as a basis of animal classification and some of them are
        discussed here.
        1>Levels of classification
        2>Symmetry
        3>Diploblastic and Tribloblastic Organization
        4>Coelem
        5>Segmentation
        6>Notochord
        7>Exit
        """)
        return int(input("Select the feature out of the given list that you want to study:"))
def levelo():
    a="level of organization".center(60).upper()
    print(a)
    print("""
    a)Cellular level of organisation: cells arranged as loose aggregates, present in Porifera (sponges)
    b)Tissue level of organisation: cells performing the same function form tissues, present in coelenterates
    c)Organ level of organisation: tissues grouped together to form an organ, which performs particular function, e.g. Platyhelminthes
    d)Organ system level of organisation: afew organs coordinatively perform a certain physiological function, e.g. Annelids, Arthropods, Molluscs, Echinoderms and Chordates
    e)Open circulatory system: cells and tissue directly receive the blood pumping out of the heart
    f)Closed circulatory system: blood is circulated through arteries, veins and capillaries
    """)
    input("Press any key to continue")
    
def symmetry():
    b="symmetry".center(60).upper()
    print(b)
    print("""
    a)Asymmetrical: no line of symmetry in the body, e.g. sponges
    b)Radial symmetry: any plane passing through centre divides the body in two symmetrical halves, e.g. coelenterates, ctenophores
    c)Bilateral symmetry: a plane divides the body in symmetrical left and right halves, e.g. annelids, arthropods, etc.
    d)Echinoderms exhibit radial as well as bilateral symmetry at different stages of their life""")
    input("Press any key to continue")
def dandto():
    c="Diploblastic and Tribloblastic Organization".center(60).upper()
    print(c)
    print("""
    a)Diploblastic: embryo with two germinal layers called external ectoderm and internal endoderm, e.g. Porifera, Cnidaria
    b)Triploblastic: embryo with three germinal layers, mesoderm between ectoderm and endoderm, e.g. Platyhelminthes to Chordates""")
    input("Press any key to continue")
def coelem():
    d="coelem".center(60).upper()
    print(d)
    print("""
    a)Body cavity between the body wall and gut wall, lined by mesoderm is called coelom
    b)Acoelomates: body cavity is absent, e.g. Platyhelminthes
    c)Pseudocoelomates: mesoderm is present as scattered pouches, e.g. Aschelminthes
    d)Coelomates: having coelom (body cavity) e.g. from Annelida to Chordata""")
    input("Press any key to continue")
def segmentation():
    e="Segmentation".center(60).upper()
    print(e)
    print("""
    a)Body cavity between the body wall and gut wall, lined by mesoderm is called coelom
    b)Acoelomates: body cavity is absent, e.g. Platyhelminthes
    c)Pseudocoelomates: mesoderm is present as scattered pouches, e.g. Aschelminthes
    d)Coelomates: having coelom (body cavity) e.g. from Annelida to Chordata""")
    input("Press any key to continue")
def notochord():
    f="NOTOCHORD".center(60).upper()
    print(f)
    print("""
    a)Body cavity between the body wall and gut wall, lined by mesoderm is called coelom
    b)Acoelomates: body cavity is absent, e.g. Platyhelminthes
    c)Pseudocoelomates: mesoderm is present as scattered pouches, e.g. Aschelminthes
    d)Coelomates: having coelom (body cavity) e.g. from Annelida to Chordata""")
    input("Press any key to continue")


def classification():
    while True:
        choice=basicmenu()
        if choice==1:
            levelo()
        elif choice==2:
            symmetry()
        elif choice==3:
            dandto()
        elif choice==4:
            coelem()
        elif choice==5:
            segmentation()
        elif choice==6:
            notochord()
        else: 
            print("You are well versed with the basis of classifiation topic now you can go for CLASSIFICATION OF ANIMALS.byee!!!!")
            break


# ashwini's function 

def phylummenu():
    print("Classification of Animals.")
    print('''
    Phylums
    1.Porifera
    2.Cnidaria
    3.Ctenophora
    4.Platyhelminthes
    5.Aschelminthes
    6.Annelida
    7.Arthrooda
    8.Mollusca
    9.Echinodermata
    10.hemichordata
    11.Chordata
    12.Exit
    ''')
    return int(input("Enter the number of phylum you want to go for from the above list"))

       
def Porifera():
    print('''
    Unique features of Phylum Porifera
    1.Porifera means Pore bearing
    2.Marine, asymmetrical with the cellular level of organisation
    3.Food intake, gaseous exchange and excretion occurs through the water transport system
    4.Water enters through pores called Ostia and goes out through osculum via central cavity known as spongocoel
    5.Spongocoel is lined by collar cells or choanocytes
    6.Intracellular digestion
    7.Body skeleton is made up of spongin fibres or spicules
    8.sponges are hermaphrodite
    9.Reproduce asexually by fragmentation and sexually by the formation of gametes
    10.Fertilisation is internal and the development of zygote goes through a distinct larval stage
    Examples: Spongilla (freshwater sponge), Euspongia (bath sponge), Sycon,
    ''')
    input('Press Any Key to Continue !!!')
def cnidaria():
    head = 'UNIQUE FEATUES OF PHYLUM CNIDARIA'
    print(head.center(60))
    print('''
    1.Aquatic, sessile or free-swimming, tissue level of organisation, diploblastic and radially symmetrical and acoelomate
    2.The central gastro-vascular cavity has a single opening called hypostome, which is surrounded by sensory tentacles
    3.Cnidoblasts are present on the tentacles, which contain nematocysts
    4.Digestion is extracellular and intracellular
    5.Corals have calcium carbonate skeleton
    6.A polyp is a scessile and cylindrical form, e.g Hydra, Adamsia
    7.Medusa is an umbrella-shaped free-swimming form, e.g. Aurelia (jellyfish)
    8.In some coelenterates, e.g. Obelia alternation of generation (metagenesis) exist. Polyp form produces medusae asexually and medusae produce polyp sexually
    9.Examples: Meandrina (Brain coral), Adamsia (Sea anemone), Gorgonia (Sea-fan), Physalia (Portuguese man of war)
   ''')
    input('Press Any Key to Continue !!!')

def ctenophora():
    head = 'UNIQUE FEATURES OF PHYLUM CTENOPHORA'
    print(head.center(60))
    print('''
    1.Marine, tissue level of organisation, diploblastic  radially symmetrical  acoelomate
    2.Eight rows of ciliated comb plates present externally
    3.Digestion is extracellular  intracellular
    4.Bioluminescence is present
    5.Hermaphrodite
    6.Sexual reproduction, fertilisation is external with indirect development
    7.Examples: Ctenoplana, Pleurobrachia
    ''')
    input('Press Any Key to Continue !!!')
def platyhelminthes():
    print('''
    1.Mostly endoparasites, dorsoventrally flattened body, triploblastic, bilaterally symmetrical, acoelomate with organ level of organisation
    2.Hooks and suckers are present in parasites
    3.Flame cells are present, which helps in osmoregulation and excretion
    4.Hermaphrodite and monoecious
    5.Internal fertilisation and indirect development through many larval stages
    6.Planaria can regenerate
    7.Examples: Fasciola Liver fluke, Taenia tapeworm  
    ''')
    input('Press Any Key to Continue !!!')

def aschelminthes():
    head = 'UNIQUE FEATURES OF PHYLUM ASCHELMINTHES'
    print(head.center(60))
    print('''
    Unique features of Phylum Aschelminthes
    Free-living or parasitic, aquatic or terrestrial
    Round body in cross-section, bilaterally symmetrical, triploblastic, pseudocoelomate with organ system organisation
    The alimentary canal is complete and has a muscular pharynxDioecious, females are longer than males
    Internal fertilisation with direct or indirect development
    Examples: Ascaris (roundworm), Wuchereria (Filarial worm), Ancylostoma (hookworm)
    ''')
    input('Press Any Key to Continue !!!')

def annelida():
    head = 'UNIQUE FEATURES OF PHYLUM ANNELIDA'
    print(head.center(60))
    print('''
    Bilaterally symmetrical, triploblastic, coelomate, organ system organisation
    Metamerically segmented
    Longitudinal and circular muscles help in locomotion
    Nereis, an aquatic animal has appendages called parapodia, which help in swimming
    Closed circulatory system
    Nephridia is present for osmoregulation and excretion
    Paired ganglia are present, which are connected to double ventral nerve cord by lateral nerves
    Reproduction is sexual. Nereis is dioecious, earthworm and leeches are monoecious
    Examples: Pheretima (earthworm), Nereis, Hirudinaria (bloodsucking leech)
    ''')
    input('Press Any Key to Continue !!!')
def arthropoda():
    head = 'UNIQUE FEATURES OF PHYLUM ARTHROPODA'
    print(head.center(60))
    print('''
    Bilaterally symmetrical, triploblastic, coelomate, organ system organisation
    Metamerically segmented
    Longitudinal and circular muscles help in locomotion
    Nereis, an aquatic animal has appendages called parapodia, which help in swimming
    Closed circulatory system
    Nephridia is present for osmoregulation and excretion
    Paired ganglia are present, which are connected to double ventral nerve cord by lateral nerves
    Reproduction is sexual. Nereis is dioecious, earthworm and leeches are monoecious
    Examples: Pheretima (earthworm), Nereis, Hirudinaria (bloodsucking leech)
    ''')
    input('Press Any Key to Continue !!!')

def mollusca():
    head = 'UNIQUE FEATURES OF PHYLUM MOLLUSCA'
    print(head.center(60))
    print('''
    Bilaterally symmetrical, triploblastic, coelomate, organ system organisation
    Unsegmented body covered with a calcareous shell
    Distinct head, muscular foot and the visceral hump is present
    Respiratory and excretory functions are executed by feather-like gills
    The radula is a rasping organ for feeding
    They are dioecious, oviparous with indirect development
    Examples: Pila (apple snail), Octopus (devilfish), Loligo (squid), Sepia (cuttlefish), Pinctada (pearl oyster)
    ''')
    input('Press Any Key to Continue !!!')


def echinodermata():
    head = 'UNIQUE FEATURES OF PHYLUM ECHINODERMATA'
    print(head.center(60))
    print('''
    Unique features of Phylum Echinodermata
    Adult- radially symmetrical, larvae- bilaterally symmetrical
    Triploblastic and coelomate
    Endoskeleton of calcareous ossicles
    The mouth is present on the ventral side and anus on the dorsal side
    The characteristic feature is the presence of Water vascular system, which helps in feeding, locomotion and respiration
    Dioecious, external fertilisation with indirect development
    Examples: Asterias (starfish), Ophiura (brittle star), Antedon (sea lily), Echinus (sea urchin)
    ''')
    input('Press Any Key to Continue !!!')

def hemichordata():
    head = 'UNIQUE FEATURES OF PHYLUM HEMICHORDATA'
    print(head.center(60))
    print('''
    Presence of stomochord, a structure similar to the notochord
    Bilaterally symmetrical, triploblastic, coelomate, organ system organisation
    Cylindrical body with a proboscis, a collar and a long trunk
    Gills are present and circulation is open type
    Proboscis gland works as an excretory organ
    Dioecious, external fertilisation with indirect development
    Examples: Balanoglossus, Saccoglossus
    ''')
    input('Press Any Key to Continue !!!')

def chordata():
    head = 'UNIQUE FEATURES OF PHYLUM CHORDATA'
    print(head.center(60))
    print('''
    Characteristic features are a dorsal hollow nerve cord, a notochord and paired gill slits
    Bilaterally symmetrical, triploblastic, coelomate, organ system organisation
    The circulatory system is closed and the post-anal tail is present
    Three subphylums come under Chordata:
    Urochordata - notochord present only in the larval tail, e.g. Ascidia, Salpa, Doliolum
    Cephalochordata  notochord present throughout life from head to tail, e.g. Branchiostoma (Lancelet or amphioxus)
    Vertebrata - Notochord is present in the embryonic stage, it gets replaced by Vertebral Column
    Vertebrata is further divided into two divisions
    Agnatha (without jaws): Class Cyclostomata
    Gnathostomata (with jaws): has two Super Class:
    Pisces (bear fins): two Classes- Chondrichthyes, Osteichthyes
    Tetrapoda (bear limbs): four classes- Amphibia, Reptilia, Aves and mammals)
    ''')
    input('Press Any Key to Continue !!!')


def phylum():
    while True:
        topic = phylummenu()
        if (topic == 1):
            Porifera()
        elif (topic == 2):
            cnidaria()
        elif (topic == 3):
            ctenophora()
        elif (topic == 4):
            platyhelminthes()
        elif (topic == 5):
            aschelminthes()
        elif (topic == 6):
            annelida()
        elif (topic == 7):
            arthropoda()
        elif (topic == 8):
            mollusca()
        elif (topic == 9):
            echinodermata()
        elif (topic == 10):
            hemichordata()
        elif (topic == 11):
            chordata()
        elif (topic == 12):
            print('''byeeee    ''')
            break

while True:
    choice = menu1()
    if choice == 1:
        classification()
    elif choice == 2:
        phylum()