import menu

def get_scores():
    arquivo = open("ranking.txt", "r")
    texto = arquivo.readline()
    arquivo.close()
    
    scores = []
    score = ""
    for i in texto:
        if i == "#":
            scores.append(score)
            score = ""
        else:
            score += i
    return scores
            
def ordena_scores(scores):
    for i in enumerate(scores):
        for j in range(0, len(scores)-1):
            if int(scores[j][-1]) < int(scores[j+1][-1]):
                temp = scores[j]
                scores[j] = scores[j+1]
                scores[j+1] = temp
    return scores
    

def main():
    print "<<<   RANKING    >>>\n"
    escores = ordena_scores(get_scores())
    for i, escore in enumerate(escores):
        print str(i+1) + ". " + escore
        
    print "\n<<<              >>>\n"
    
    menu.main()
    
    
