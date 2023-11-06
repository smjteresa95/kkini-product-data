class CalNutriFilter:

    def __init__(self, category, kcal, carb, protein, fat, sodium, cholesterol, sat_fat, trans_fat, sugar):
        self.category = category
        self.kcal = float(kcal)
        self.carb = float(carb)
        self.protein = float(protein)
        self.fat = float(fat)
        self.sodium = float(sodium)
        self.cholesterol = float(cholesterol)
        self.sat_fat = float(sat_fat)
        self.trans_fat = float(trans_fat)
        self.sugar = float(sugar)

        self.calculate_nutri_conditions()


    def calculate_nutri_conditions(self):
        self.conditions = {}
        serving_size = 100

        #is_low_calorie
        self.conditions['is_low_calorie'] = ((self.category == '음료') and (int(self.kcal) < 20)) | ((self.category != '음료') and (int(self.kcal) < 40))

        #is_high_calorie
        self.conditions['is_high_calorie'] = ((self.kcal > 500) and (self.sodium > 600))

        #is_sugar_free
        self.conditions['is_sugar_free'] = self.sugar <= 1

        #is_low_sugar
        self.conditions['is_low_sugar'] = self.sugar <= serving_size*0.05

        #is_low_carb
        self.conditions['is_low_carb'] = self.carb >= serving_size*0.11

        #is_high_carb
        self.conditions['is_high_carb'] = self.carb > serving_size*0.6

        #is_keto
        self.conditions['is_keto'] = self.carb <= serving_size*0.2

        #is_low_transfat
        self.conditions['is_low_transfat'] = self.trans_fat <= 1

        #is_high_protein
        self.conditions['is_high_protein'] = self.protein >= serving_size*0.2

        #is_low_sodium
        self.conditions['is_low_sodium'] = self.sodium <= serving_size*2

        #is_low_cholesterol
        self.conditions['is_low_cholesterol'] = self.cholesterol < 300
        
        #is_low_sat_fat
        self.conditions['is_low_set_fat'] = self.sat_fat <= serving_size*0.02

        #is_low_fat
        self.conditions['is_low_fat'] = self.fat <= 3.0

        #is_high_fat
        self.conditions['is_high_fat'] = self.fat > serving_size * 0.2


    def get_is_green(self):
        green_true = sum(self.conditions.values())
        return green_true >= 5
    

    def get_nutri_filter(self):
        filter_list = list(self.conditions.values())
        is_green = self.get_is_green()
        filter_list.append(is_green)
        return filter_list
    

    def get_nut_score(self):
        nut_score = 0.0  # Initialize score to 0
        serving_size = 100
        
        if self.category == '음료':
            if self.kcal <= 0:
                nut_score += 5
            elif self.kcal <= 5:
                nut_score += 4
            elif self.kcal <= 10:
                nut_score += 3
            elif self.kcal <= 15:
                nut_score += 2
            elif self.kcal <= 20:
                nut_score += 1
        else:
            if self.kcal < 20:
                nut_score += 5
            elif self.kcal < 25:
                nut_score += 4
            elif self.kcal < 30:
                nut_score += 3
            elif self.kcal < 35:
                nut_score += 2
            elif self.kcal < 40:
                nut_score += 1
    
        # Scoring for sugar
        sugar_percentage = (self.sugar / serving_size) * 100
        if sugar_percentage <= 1:
            nut_score += 5
        elif sugar_percentage <= 2:
            nut_score += 4
        elif sugar_percentage <= 3:
            nut_score += 3
        elif sugar_percentage <= 4:
            nut_score += 2
        elif sugar_percentage <= 5:
            nut_score += 1
        
        # Scoring for Carbohydrate
        carb_percentage = (self.carb / serving_size) * 100
        if carb_percentage <= 12:
            nut_score += 5
        elif carb_percentage <= 15:
            nut_score += 4
        elif carb_percentage <= 18:
            nut_score += 3
        elif carb_percentage <= 20:
            nut_score += 2
        else:
            nut_score += 1

        # Scoring for transFat
        if self.trans_fat < 1:
            nut_score += 5

        # Scoring for protein
        protein_percentage = (self.protein / serving_size) * 100
        if protein_percentage >= 28:
            nut_score += 5
        elif protein_percentage >= 26:
            nut_score += 4
        elif protein_percentage >= 24:
            nut_score += 3
        elif protein_percentage >= 22:
            nut_score += 2
        elif protein_percentage >= 20:
            nut_score += 1
        
        # Scoring for sodium
        if self.sodium <= 2 * serving_size:
            nut_score += 5
        elif self.sodium <= 1.5 * serving_size:
            nut_score += 4
        elif self.sodium <= serving_size:
            nut_score += 3
        elif self.sodium <= 0.5 * serving_size:
            nut_score += 2
        else:
            nut_score += 1

        # Scoring for cholesterol
        if self.cholesterol < 220:
            nut_score += 5
        elif self.cholesterol < 240:
            nut_score += 4
        elif self.cholesterol < 260:
            nut_score += 3
        elif self.cholesterol < 280:
            nut_score += 2
        elif self.cholesterol < 300:
            nut_score += 1

        # Scoring for saturatedFat
        saturated_fat_percentage = (self.sat_fat / serving_size) * 100
        if saturated_fat_percentage <= 1:
            nut_score += 5
        elif saturated_fat_percentage <= 1.5:
            nut_score += 4
        elif saturated_fat_percentage <= 2:
            nut_score += 3
        else:
            nut_score += 2
        
        # Scoring for fat
        fat_percentage = (self.fat / serving_size) * 100
        if self.category == "음료":
            if fat_percentage <= 0.5:
                nut_score += 5
            elif fat_percentage <= 1:
                nut_score += 4
            elif fat_percentage <= 1.5:
                nut_score += 3
            else:
                nut_score += 2
        else:
            if fat_percentage <= 1:
                nut_score += 5
            elif fat_percentage <= 1.5:
                nut_score += 4
            elif fat_percentage <= 2:
                nut_score += 3
            elif fat_percentage <= 2.5:
                nut_score += 2
            elif fat_percentage <= 3:
                nut_score += 1
        
        return nut_score



    # def get_nutri_filter(self):
    #     nutri_filter = []
    #     green_true = 0
    #     serving_size = 100

    #     #is_low_calorie
    #     if ((self.category == '음료') and (self.kcal < 20)) | ((self.category != '음료') and (self.kcal < 40)):
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_high_calorie
    #     if (self.kcal > 500) & (self.sodium > 600):
    #         nutri_filter.append(True)
    #     else:
    #         nutri_filter.append(False)

    #     #is_sugar_free
    #     if self.sugar <= 1:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)
        
    #     #is_low_sugar
    #     if self.sugar <= serving_size*0.05:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_low_carb
    #     if self.carb >= serving_size*0.11:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_high_carb
    #     if self.carb > serving_size*0.6:
    #         nutri_filter.append(True)
    #     else:
    #         nutri_filter.append(False)

    #     #is_keto
    #     if self.carb <= serving_size*0.2:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_low_transfat
    #     if self.trans_fat <= 1:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_high_protein
    #     if self.protein >= serving_size*0.2:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_low_sodium
    #     if self.sodium <= serving_size*2:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_low_cholesterol
    #     if self.cholesterol < 300:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_low_sat_fat
    #     if self.sat_fat <= serving_size*0.02:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_low_fat
    #     if self.fat <= 3.0:
    #         nutri_filter.append(True)
    #         green_true+=1
    #     else:
    #         nutri_filter.append(False)

    #     #is_high_fat
    #     if self.fat > serving_size * 0.2:
    #         nutri_filter.append(True)
    #     else:
    #         nutri_filter.append(False)
        
    #     #is_green
    #     is_green = (green_true >= 5)
    #     if is_green:
    #         nutri_filter.append(True)
    #     else:
    #         nutri_filter.append(False)

        
    #     return nutri_filter

