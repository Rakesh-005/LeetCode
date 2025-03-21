class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        answer = []
        flag = True
        
        while flag:
            flag = False
            for i in range(len(recipes)):
                if recipes[i] not in supplies:
                    if all(item in supplies for item in ingredients[i]):
                        supplies.add(recipes[i])
                        answer.append(recipes[i])
                        flag = True
                        
        return answer