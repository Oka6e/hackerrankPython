def students_avg_score(X):
    all_scores = []
    
    for _ in range(X):
        sub_scores = map(float, input().split())
        all_scores.append(sub_scores)
    
    for i in zip(*all_scores):
        print(sum(i)/len(i))
    

if __name__ == '__main__':
    N, X = map(int, input().split()) # N = Student number; X = Subject Number
    students_avg_score(X)
