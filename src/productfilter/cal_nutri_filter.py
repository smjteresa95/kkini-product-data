class CalNutriFilter:

    def __init__(self, category, kcal, carb, protein, fat, sodium, cholesterol, sat_fat, trans_fat, sugar):
        self.category = category
        self.kcal = kcal
        self.carb = carb
        self.protein = protein
        self.fat = fat
        self.sodium = sodium
        self.cholesterol = cholesterol
        self.sat_fat = sat_fat
        self.trans_fat = trans_fat
        self.sugar = sugar
    
    def get_nutri_filter(self):
        nutri_filter = []
        green_true = 0
        serving_size = 100

        #is_low_calorie
        if ((self.category == '음료') and (self.kcal < 20)) | ((self.category != '음료') and (self.kcal < 40)):
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_high_calorie
        if (self.kcal > 500) & (self.sodium > 600):
            nutri_filter.append(True)
        else:
            nutri_filter.append(False)

        #is_sugar_free
        if self.sugar <= 1:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)
        
        #is_low_sugar
        if self.sugar <= serving_size*0.05:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_low_carb
        if self.carb >= serving_size*0.11:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_high_carb
        if self.carb > serving_size*0.6:
            nutri_filter.append(True)
        else:
            nutri_filter.append(False)

        #is_keto
        if self.carb <= serving_size*0.2:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_low_transfat
        if self.trans_fat <= 1:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_high_protein
        if self.protein >= serving_size*0.2:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_low_sodium
        if self.sodium <= serving_size*2:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_low_cholesterol
        if self.cholesterol < 300:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_low_sat_fat
        if self.sat_fat <= serving_size*0.02:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_low_fat
        if self.fat <= 3.0:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        #is_high_fat
        if self.fat > serving_size * 0.2:
            nutri_filter.append(True)
        else:
            nutri_filter.append(False)
        
        if green_true >= 5:
            nutri_filter.append(True)
            green_true+=1
        else:
            nutri_filter.append(False)

        
        return nutri_filter










    



    