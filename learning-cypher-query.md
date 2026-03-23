
//making Fully Normalized Graph 
//Graph Data Modeling
MATCH (n) DETACH DELETE n;

// Create the Directory Root
MERGE (m:Management {name: "Staff Directory"})

// Create the 5 Specialist Groups
MERGE (ind:SpecialistGroup {cuisine: "Indian"})
MERGE (mex:SpecialistGroup {cuisine: "Mexican"})
MERGE (ita:SpecialistGroup {cuisine: "Italian"})
MERGE (spa:SpecialistGroup {cuisine: "Spanish"})
MERGE (jap:SpecialistGroup {cuisine: "Japanese"})

// Link Groups to the Root Directory
WITH m, ind, mex, ita, spa, jap
MERGE (m)-[:MANAGES]->(ind)
MERGE (m)-[:MANAGES]->(mex)
MERGE (m)-[:MANAGES]->(ita)
MERGE (m)-[:MANAGES]->(spa)
MERGE (m)-[:MANAGES]->(jap);

// Indian Team
MERGE (e1:Employee {name: "Arjun"})
MERGE (e2:Employee {name: "Priya"})
MERGE (e3:Employee {name: "Rahul"})
WITH e1, e2, e3 MATCH (g:SpecialistGroup {cuisine: "Indian"})
MERGE (e1)-[:WORKS_AS]->(g) MERGE (e2)-[:WORKS_AS]->(g) MERGE (e3)-[:WORKS_AS]->(g);

// Mexican Team
MERGE (e4:Employee {name: "Carlos"})
MERGE (e5:Employee {name: "Elena"})
MERGE (e6:Employee {name: "Mateo"})
WITH e4, e5, e6 MATCH (g:SpecialistGroup {cuisine: "Mexican"})
MERGE (e4)-[:WORKS_AS]->(g) MERGE (e5)-[:WORKS_AS]->(g) MERGE (e6)-[:WORKS_AS]->(g);

// Italian Team
MERGE (e7:Employee {name: "Sofia"})
MERGE (e8:Employee {name: "Giovanni"})
MERGE (e9:Employee {name: "Luca"})
WITH e7, e8, e9 MATCH (g:SpecialistGroup {cuisine: "Italian"})
MERGE (e7)-[:WORKS_AS]->(g) MERGE (e8)-[:WORKS_AS]->(g) MERGE (e9)-[:WORKS_AS]->(g);

// Spanish Team
MERGE (e10:Employee {name: "Isabella"})
MERGE (e11:Employee {name: "Diego"})
MERGE (e12:Employee {name: "Carmen"})
WITH e10, e11, e12 MATCH (g:SpecialistGroup {cuisine: "Spanish"})
MERGE (e10)-[:WORKS_AS]->(g) MERGE (e11)-[:WORKS_AS]->(g) MERGE (e12)-[:WORKS_AS]->(g);

// Japanese Team
MERGE (e13:Employee {name: "Kenji"})
MERGE (e14:Employee {name: "Yuki"})
MERGE (e15:Employee {name: "Hiro"})
WITH e13, e14, e15 MATCH (g:SpecialistGroup {cuisine: "Japanese"})
MERGE (e13)-[:WORKS_AS]->(g) MERGE (e14)-[:WORKS_AS]->(g) MERGE (e15)-[:WORKS_AS]->(g);

// 1. Ensure the Anchor Node exists
MERGE (f:Food {name: "Restaurant Food"})

// 2. Create/Verify Categories (Using MERGE here ensures they actually exist)
MERGE (c1:Category {name: "Grains & Bowls"})
MERGE (c2:Category {name: "Protein Grills"})
MERGE (c3:Category {name: "Leafy Greens"})
MERGE (c4:Category {name: "Probiotic & Fermented"})
MERGE (c5:Category {name: "Hearty Soups"})
MERGE (c6:Category {name: "Quick Bites"})
MERGE (c7:Category {name: "Hydration & Drinks"})
MERGE (c8:Category {name: "Plant-Based"})
MERGE (c9:Category {name: "Keto-Friendly"})
MERGE (c10:Category {name: "Guilt-Free Treats"})

// 3. Link them to the Anchor
WITH f, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10
MERGE (f)-[:HAS_CATEGORY]->(c1)
MERGE (f)-[:HAS_CATEGORY]->(c2)
MERGE (f)-[:HAS_CATEGORY]->(c3)
MERGE (f)-[:HAS_CATEGORY]->(c4)
MERGE (f)-[:HAS_CATEGORY]->(c5)
MERGE (f)-[:HAS_CATEGORY]->(c6)
MERGE (f)-[:HAS_CATEGORY]->(c7)
MERGE (f)-[:HAS_CATEGORY]->(c8)
MERGE (f)-[:HAS_CATEGORY]->(c9)
MERGE (f)-[:HAS_CATEGORY]->(c10);

//create nodes for each property
// 1. Type Nodes
MERGE (veg:Type {name: "Veg"})
MERGE (nonVeg:Type {name: "Non-Veg"})

// 2. Common Price Nodes (We will add more as needed)
MERGE (p200:Price {value: 200})
MERGE (p300:Price {value: 300})
MERGE (p400:Price {value: 400})
MERGE (p500:Price {value: 500})

// 3. Nutritional Value Hubs (Grouped by health benefit)
MERGE (nHighProt:Nutrition {label: "High Protein"})
MERGE (nLowCal:Nutrition {label: "Low Calorie"})
MERGE (nFiber:Nutrition {label: "High Fiber"})
MERGE (nAntiox:Nutrition {label: "Antioxidant Rich"})


// 1. Create Cuisine Nodes (Cultural Knowledge)
MERGE (c_ind:Cuisine {name: "Indian"})
MERGE (c_mex:Cuisine {name: "Mexican"})
MERGE (c_ita:Cuisine {name: "Italian"})
MERGE (c_spa:Cuisine {name: "Spanish"})
MERGE (c_jap:Cuisine {name: "Japanese"})

// 2. Ensure Specialist Groups exist (Staffing Logic)
MERGE (g_ind:SpecialistGroup {cuisine: "Indian"})
MERGE (g_mex:SpecialistGroup {cuisine: "Mexican"})
MERGE (g_ita:SpecialistGroup {cuisine: "Italian"})
MERGE (g_spa:SpecialistGroup {cuisine: "Spanish"})
MERGE (g_jap:SpecialistGroup {cuisine: "Japanese"})

// 3. Link them together
WITH c_ind, c_mex, c_ita, c_spa, c_jap, g_ind, g_mex, g_ita, g_spa, g_jap
MERGE (g_ind)-[:EXPERTS_IN]->(c_ind)
MERGE (g_mex)-[:EXPERTS_IN]->(c_mex)
MERGE (g_ita)-[:EXPERTS_IN]->(c_ita)
MERGE (g_spa)-[:EXPERTS_IN]->(c_spa)
MERGE (g_jap)-[:EXPERTS_IN]->(c_jap);


// 1. Ensure the Master Anchor exists
MERGE (mi:MasterIngredient {name: "Ingredients List"})

// 2. Add WITH to bridge to the UNWIND
WITH mi
UNWIND [
  "Basmati Rice", "Quinoa", "Chicken", "Salmon", "Chickpeas", 
  "Beef", "Seaweed", "Shrimp", "Paneer", "Avocado",
  "Tofu", "Miso", "Tomato", "Pasta", "Olive Oil", 
  "Saffron", "Turmeric", "Corn", "Jalapenos", "Black Beans",
  "Kale", "Spinach", "Arugula", "Walnuts", "Feta Cheese",
  "Kimchi", "Sauerkraut", "Yogurt", "Tempeh", "Lemon"
] AS ing_name

// 3. Create the Ingredients and link them
MERGE (i:Ingredient {name: ing_name})
MERGE (mi)-[:LISTS]->(i);

// # now we are gonna create 10 dishes for each category # 


//-----------------------------------------------------------------------------------------------------------------


// 1. FETCH GLOBAL HUBS
// ADD WITH clause here before MATCH
WITH 1 as dummy
MATCH (cat1:Category {name: "Grains & Bowls"})
MATCH (veg:Type {name: "Veg"}), (nv:Type {name: "Non-Veg"})
MATCH (p300:Price {value: 300}), (p400:Price {value: 400}), (p500:Price {value: 500})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (nProt:Nutrition {label: "High Protein"}), (nAntiox:Nutrition {label: "Antioxidant Rich"})
MATCH (c_ind:Cuisine {name: "Indian"}), (c_mex:Cuisine {name: "Mexican"}), (c_jap:Cuisine {name: "Japanese"}), (c_spa:Cuisine {name: "Spanish"})

// 2. THE UNIVERSAL SUITCASE
WITH cat1, veg, nv, p300, p400, p500, nFiber, nProt, nAntiox, c_ind, c_mex, c_jap, c_spa

// 3. CREATE DISHES 1-10 (Using ONLY your 30 Master Ingredients)

// Dish 1
MERGE (d1:Dish {name: "Turmeric Basmati Bowl"})
  MERGE (d1)-[:BELONGS_TO]->(cat1) MERGE (d1)-[:HAS_TYPE]->(veg) MERGE (d1)-[:COSTS]->(p300)
  MERGE (d1)-[:NUTRITIONAL_BENEFIT]->(nFiber) MERGE (d1)-[:ORIGINATES_FROM]->(c_ind)
  WITH * MATCH (i:Ingredient {name: "Basmati Rice"}) 
  MERGE (d1)-[:HAS_INGREDIENT]->(i)

// Dish 2
WITH * MERGE (d2:Dish {name: "Black Bean Taco Bowl"})
  MERGE (d2)-[:BELONGS_TO]->(cat1) MERGE (d2)-[:HAS_TYPE]->(veg) MERGE (d2)-[:COSTS]->(p400)
  MERGE (d2)-[:NUTRITIONAL_BENEFIT]->(nFiber) MERGE (d2)-[:ORIGINATES_FROM]->(c_mex)
  WITH * MATCH (i:Ingredient {name: "Black Beans"}) 
  MERGE (d2)-[:HAS_INGREDIENT]->(i)

// Dish 3
WITH * MERGE (d3:Dish {name: "Chicken Biryani Bowl"})
  MERGE (d3)-[:BELONGS_TO]->(cat1) MERGE (d3)-[:HAS_TYPE]->(nv) MERGE (d3)-[:COSTS]->(p500)
  MERGE (d3)-[:NUTRITIONAL_BENEFIT]->(nProt) MERGE (d3)-[:ORIGINATES_FROM]->(c_ind)
  WITH * MATCH (i:Ingredient {name: "Chicken"}) 
  MERGE (d3)-[:HAS_INGREDIENT]->(i)

// Dish 4
WITH * MERGE (d4:Dish {name: "Miso Salmon Bowl"})
  MERGE (d4)-[:BELONGS_TO]->(cat1) MERGE (d4)-[:HAS_TYPE]->(nv) MERGE (d4)-[:COSTS]->(p500)
  MERGE (d4)-[:NUTRITIONAL_BENEFIT]->(nProt) MERGE (d4)-[:ORIGINATES_FROM]->(c_jap)
  WITH * MATCH (i:Ingredient {name: "Salmon"}), (i2:Ingredient {name: "Miso"}) 
  MERGE (d4)-[:HAS_INGREDIENT]->(i) MERGE (d4)-[:HAS_INGREDIENT]->(i2)

// Dish 5
WITH * MERGE (d5:Dish {name: "Spanish Chickpea Bowl"})
  MERGE (d5)-[:BELONGS_TO]->(cat1) MERGE (d5)-[:HAS_TYPE]->(veg) MERGE (d5)-[:COSTS]->(p300)
  MERGE (d5)-[:NUTRITIONAL_BENEFIT]->(nFiber) MERGE (d5)-[:ORIGINATES_FROM]->(c_spa)
  WITH * MATCH (i:Ingredient {name: "Chickpeas"}) 
  MERGE (d5)-[:HAS_INGREDIENT]->(i)

// Dish 6
WITH * MERGE (d6:Dish {name: "Beef & Jalapeno Bowl"})
  MERGE (d6)-[:BELONGS_TO]->(cat1) MERGE (d6)-[:HAS_TYPE]->(nv) MERGE (d6)-[:COSTS]->(p400)
  MERGE (d6)-[:NUTRITIONAL_BENEFIT]->(nProt) MERGE (d6)-[:ORIGINATES_FROM]->(c_mex)
  WITH * MATCH (i1:Ingredient {name: "Beef"}), (i2:Ingredient {name: "Jalapenos"}) 
  MERGE (d6)-[:HAS_INGREDIENT]->(i1) MERGE (d6)-[:HAS_INGREDIENT]->(i2)

// Dish 7
WITH * MERGE (d7:Dish {name: "Seaweed Zen Bowl"})
  MERGE (d7)-[:BELONGS_TO]->(cat1) MERGE (d7)-[:HAS_TYPE]->(nv) MERGE (d7)-[:COSTS]->(p500)
  MERGE (d7)-[:NUTRITIONAL_BENEFIT]->(nAntiox) MERGE (d7)-[:ORIGINATES_FROM]->(c_jap)
  WITH * MATCH (i:Ingredient {name: "Seaweed"}) 
  MERGE (d7)-[:HAS_INGREDIENT]->(i)

// Dish 8
WITH * MERGE (d8:Dish {name: "Saffron Shrimp Bowl"})
  MERGE (d8)-[:BELONGS_TO]->(cat1) MERGE (d8)-[:HAS_TYPE]->(nv) MERGE (d8)-[:COSTS]->(p500)
  MERGE (d8)-[:NUTRITIONAL_BENEFIT]->(nProt) MERGE (d8)-[:ORIGINATES_FROM]->(c_spa)
  WITH * MATCH (i1:Ingredient {name: "Shrimp"}), (i2:Ingredient {name: "Saffron"}) 
  MERGE (d8)-[:HAS_INGREDIENT]->(i1) MERGE (d8)-[:HAS_INGREDIENT]->(i2)

// Dish 9
WITH * MERGE (d9:Dish {name: "Paneer Rice Bowl"})
  MERGE (d9)-[:BELONGS_TO]->(cat1) MERGE (d9)-[:HAS_TYPE]->(veg) MERGE (d9)-[:COSTS]->(p300)
  MERGE (d9)-[:NUTRITIONAL_BENEFIT]->(nProt) MERGE (d9)-[:ORIGINATES_FROM]->(c_ind)
  WITH * MATCH (i1:Ingredient {name: "Paneer"}), (i2:Ingredient {name: "Basmati Rice"}) 
  MERGE (d9)-[:HAS_INGREDIENT]->(i1) MERGE (d9)-[:HAS_INGREDIENT]->(i2)

// Dish 10
WITH * MERGE (d10:Dish {name: "Avocado Sushi Bowl"})
  MERGE (d10)-[:BELONGS_TO]->(cat1) MERGE (d10)-[:HAS_TYPE]->(veg) MERGE (d10)-[:COSTS]->(p400)
  MERGE (d10)-[:NUTRITIONAL_BENEFIT]->(nFiber) MERGE (d10)-[:ORIGINATES_FROM]->(c_jap)
  WITH * MATCH (i:Ingredient {name: "Avocado"}) 
  MERGE (d10)-[:HAS_INGREDIENT]->(i);

// ===== CATEGORY 2: Protein Grills (Dishes 11-20) =====

// Dish 11: Tandoori Chicken Grill
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d11:Dish {name: "Tandoori Chicken Grill"})
MERGE (d11)-[:BELONGS_TO]->(cat2)
MERGE (d11)-[:HAS_TYPE]->(nv)
MERGE (d11)-[:COSTS]->(p500)
MERGE (d11)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d11)-[:ORIGINATES_FROM]->(c_ind)
WITH d11
MATCH (i1:Ingredient {name: "Chicken"}), (i2:Ingredient {name: "Turmeric"})
MERGE (d11)-[:HAS_INGREDIENT]->(i1)
MERGE (d11)-[:HAS_INGREDIENT]->(i2);

// Dish 12: Miso Glazed Salmon
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d12:Dish {name: "Miso Glazed Salmon"})
MERGE (d12)-[:BELONGS_TO]->(cat2)
MERGE (d12)-[:HAS_TYPE]->(nv)
MERGE (d12)-[:COSTS]->(p500)
MERGE (d12)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d12)-[:ORIGINATES_FROM]->(c_jap)
WITH d12
MATCH (i1:Ingredient {name: "Salmon"}), (i2:Ingredient {name: "Miso"})
MERGE (d12)-[:HAS_INGREDIENT]->(i1)
MERGE (d12)-[:HAS_INGREDIENT]->(i2);

// Dish 13: Spanish Garlic Shrimp
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d13:Dish {name: "Spanish Garlic Shrimp"})
MERGE (d13)-[:BELONGS_TO]->(cat2)
MERGE (d13)-[:HAS_TYPE]->(nv)
MERGE (d13)-[:COSTS]->(p500)
MERGE (d13)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d13)-[:ORIGINATES_FROM]->(c_spa)
WITH d13
MATCH (i1:Ingredient {name: "Shrimp"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d13)-[:HAS_INGREDIENT]->(i1)
MERGE (d13)-[:HAS_INGREDIENT]->(i2);

// Dish 14: Mexican Beef Fajitas
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d14:Dish {name: "Mexican Beef Fajitas"})
MERGE (d14)-[:BELONGS_TO]->(cat2)
MERGE (d14)-[:HAS_TYPE]->(nv)
MERGE (d14)-[:COSTS]->(p400)
MERGE (d14)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d14)-[:ORIGINATES_FROM]->(c_mex)
WITH d14
MATCH (i1:Ingredient {name: "Beef"}), (i2:Ingredient {name: "Jalapenos"})
MERGE (d14)-[:HAS_INGREDIENT]->(i1)
MERGE (d14)-[:HAS_INGREDIENT]->(i2);

// Dish 15: Grilled Paneer Tikka
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d15:Dish {name: "Grilled Paneer Tikka"})
MERGE (d15)-[:BELONGS_TO]->(cat2)
MERGE (d15)-[:HAS_TYPE]->(veg)
MERGE (d15)-[:COSTS]->(p300)
MERGE (d15)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d15)-[:ORIGINATES_FROM]->(c_ind)
WITH d15
MATCH (i1:Ingredient {name: "Paneer"}), (i2:Ingredient {name: "Turmeric"})
MERGE (d15)-[:HAS_INGREDIENT]->(i1)
MERGE (d15)-[:HAS_INGREDIENT]->(i2);

// Dish 16: Teriyaki Chicken Skewers
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d16:Dish {name: "Teriyaki Chicken Skewers"})
MERGE (d16)-[:BELONGS_TO]->(cat2)
MERGE (d16)-[:HAS_TYPE]->(nv)
MERGE (d16)-[:COSTS]->(p400)
MERGE (d16)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d16)-[:ORIGINATES_FROM]->(c_jap)
WITH d16
MATCH (i:Ingredient {name: "Chicken"})
MERGE (d16)-[:HAS_INGREDIENT]->(i);

// Dish 17: Grilled Tofu Steaks
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d17:Dish {name: "Grilled Tofu Steaks"})
MERGE (d17)-[:BELONGS_TO]->(cat2)
MERGE (d17)-[:HAS_TYPE]->(veg)
MERGE (d17)-[:COSTS]->(p300)
MERGE (d17)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d17)-[:ORIGINATES_FROM]->(c_jap)
WITH d17
MATCH (i:Ingredient {name: "Tofu"})
MERGE (d17)-[:HAS_INGREDIENT]->(i);

// Dish 18: Saffron Grilled Shrimp
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d18:Dish {name: "Saffron Grilled Shrimp"})
MERGE (d18)-[:BELONGS_TO]->(cat2)
MERGE (d18)-[:HAS_TYPE]->(nv)
MERGE (d18)-[:COSTS]->(p500)
MERGE (d18)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d18)-[:ORIGINATES_FROM]->(c_spa)
WITH d18
MATCH (i1:Ingredient {name: "Shrimp"}), (i2:Ingredient {name: "Saffron"})
MERGE (d18)-[:HAS_INGREDIENT]->(i1)
MERGE (d18)-[:HAS_INGREDIENT]->(i2);

// Dish 19: Charred Corn Chicken
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d19:Dish {name: "Charred Corn Chicken"})
MERGE (d19)-[:BELONGS_TO]->(cat2)
MERGE (d19)-[:HAS_TYPE]->(nv)
MERGE (d19)-[:COSTS]->(p400)
MERGE (d19)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d19)-[:ORIGINATES_FROM]->(c_mex)
WITH d19
MATCH (i1:Ingredient {name: "Chicken"}), (i2:Ingredient {name: "Corn"})
MERGE (d19)-[:HAS_INGREDIENT]->(i1)
MERGE (d19)-[:HAS_INGREDIENT]->(i2);

// Dish 20: Tempeh Grill Platter
MATCH (cat2:Category {name: "Protein Grills"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d20:Dish {name: "Tempeh Grill Platter"})
MERGE (d20)-[:BELONGS_TO]->(cat2)
MERGE (d20)-[:HAS_TYPE]->(veg)
MERGE (d20)-[:COSTS]->(p300)
MERGE (d20)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d20)-[:ORIGINATES_FROM]->(c_jap)
WITH d20
MATCH (i:Ingredient {name: "Tempeh"})
MERGE (d20)-[:HAS_INGREDIENT]->(i);


// ===== CATEGORY 3: Leafy Greens (Dishes 21-30) =====

// Dish 21: Kale Caesar Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d21:Dish {name: "Kale Caesar Salad"})
MERGE (d21)-[:BELONGS_TO]->(cat3)
MERGE (d21)-[:HAS_TYPE]->(veg)
MERGE (d21)-[:COSTS]->(p300)
MERGE (d21)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d21)-[:ORIGINATES_FROM]->(c_ita)
WITH d21
MATCH (i1:Ingredient {name: "Kale"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d21)-[:HAS_INGREDIENT]->(i1)
MERGE (d21)-[:HAS_INGREDIENT]->(i2);

// Dish 22: Spinach Paneer Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d22:Dish {name: "Spinach Paneer Salad"})
MERGE (d22)-[:BELONGS_TO]->(cat3)
MERGE (d22)-[:HAS_TYPE]->(veg)
MERGE (d22)-[:COSTS]->(p300)
MERGE (d22)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d22)-[:ORIGINATES_FROM]->(c_ind)
WITH d22
MATCH (i1:Ingredient {name: "Spinach"}), (i2:Ingredient {name: "Paneer"})
MERGE (d22)-[:HAS_INGREDIENT]->(i1)
MERGE (d22)-[:HAS_INGREDIENT]->(i2);

// Dish 23: Arugula Walnut Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d23:Dish {name: "Arugula Walnut Salad"})
MERGE (d23)-[:BELONGS_TO]->(cat3)
MERGE (d23)-[:HAS_TYPE]->(veg)
MERGE (d23)-[:COSTS]->(p300)
MERGE (d23)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d23)-[:ORIGINATES_FROM]->(c_ita)
WITH d23
MATCH (i1:Ingredient {name: "Arugula"}), (i2:Ingredient {name: "Walnuts"})
MERGE (d23)-[:HAS_INGREDIENT]->(i1)
MERGE (d23)-[:HAS_INGREDIENT]->(i2);

// Dish 24: Seaweed Salad Bowl
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d24:Dish {name: "Seaweed Salad Bowl"})
MERGE (d24)-[:BELONGS_TO]->(cat3)
MERGE (d24)-[:HAS_TYPE]->(veg)
MERGE (d24)-[:COSTS]->(p300)
MERGE (d24)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d24)-[:ORIGINATES_FROM]->(c_jap)
WITH d24
MATCH (i:Ingredient {name: "Seaweed"})
MERGE (d24)-[:HAS_INGREDIENT]->(i);

// Dish 25: Spinach Feta Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d25:Dish {name: "Spinach Feta Salad"})
MERGE (d25)-[:BELONGS_TO]->(cat3)
MERGE (d25)-[:HAS_TYPE]->(veg)
MERGE (d25)-[:COSTS]->(p300)
MERGE (d25)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d25)-[:ORIGINATES_FROM]->(c_spa)
WITH d25
MATCH (i1:Ingredient {name: "Spinach"}), (i2:Ingredient {name: "Feta Cheese"})
MERGE (d25)-[:HAS_INGREDIENT]->(i1)
MERGE (d25)-[:HAS_INGREDIENT]->(i2);

// Dish 26: Kale Chickpea Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d26:Dish {name: "Kale Chickpea Salad"})
MERGE (d26)-[:BELONGS_TO]->(cat3)
MERGE (d26)-[:HAS_TYPE]->(veg)
MERGE (d26)-[:COSTS]->(p300)
MERGE (d26)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d26)-[:ORIGINATES_FROM]->(c_ind)
WITH d26
MATCH (i1:Ingredient {name: "Kale"}), (i2:Ingredient {name: "Chickpeas"})
MERGE (d26)-[:HAS_INGREDIENT]->(i1)
MERGE (d26)-[:HAS_INGREDIENT]->(i2);

// Dish 27: Arugula Salmon Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d27:Dish {name: "Arugula Salmon Salad"})
MERGE (d27)-[:BELONGS_TO]->(cat3)
MERGE (d27)-[:HAS_TYPE]->(nv)
MERGE (d27)-[:COSTS]->(p400)
MERGE (d27)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d27)-[:ORIGINATES_FROM]->(c_ita)
WITH d27
MATCH (i1:Ingredient {name: "Arugula"}), (i2:Ingredient {name: "Salmon"})
MERGE (d27)-[:HAS_INGREDIENT]->(i1)
MERGE (d27)-[:HAS_INGREDIENT]->(i2);

// Dish 28: Spinach Avocado Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d28:Dish {name: "Spinach Avocado Salad"})
MERGE (d28)-[:BELONGS_TO]->(cat3)
MERGE (d28)-[:HAS_TYPE]->(veg)
MERGE (d28)-[:COSTS]->(p300)
MERGE (d28)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d28)-[:ORIGINATES_FROM]->(c_mex)
WITH d28
MATCH (i1:Ingredient {name: "Spinach"}), (i2:Ingredient {name: "Avocado"})
MERGE (d28)-[:HAS_INGREDIENT]->(i1)
MERGE (d28)-[:HAS_INGREDIENT]->(i2);

// Dish 29: Kale Tofu Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d29:Dish {name: "Kale Tofu Salad"})
MERGE (d29)-[:BELONGS_TO]->(cat3)
MERGE (d29)-[:HAS_TYPE]->(veg)
MERGE (d29)-[:COSTS]->(p300)
MERGE (d29)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d29)-[:ORIGINATES_FROM]->(c_jap)
WITH d29
MATCH (i1:Ingredient {name: "Kale"}), (i2:Ingredient {name: "Tofu"})
MERGE (d29)-[:HAS_INGREDIENT]->(i1)
MERGE (d29)-[:HAS_INGREDIENT]->(i2);

// Dish 30: Arugula Tomato Salad
MATCH (cat3:Category {name: "Leafy Greens"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d30:Dish {name: "Arugula Tomato Salad"})
MERGE (d30)-[:BELONGS_TO]->(cat3)
MERGE (d30)-[:HAS_TYPE]->(veg)
MERGE (d30)-[:COSTS]->(p200)
MERGE (d30)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d30)-[:ORIGINATES_FROM]->(c_ita)
WITH d30
MATCH (i1:Ingredient {name: "Arugula"}), (i2:Ingredient {name: "Tomato"})
MERGE (d30)-[:HAS_INGREDIENT]->(i1)
MERGE (d30)-[:HAS_INGREDIENT]->(i2);


// ===== CATEGORY 4: Probiotic & Fermented (Dishes 31-40) =====

// Dish 31: Kimchi Rice Bowl
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d31:Dish {name: "Kimchi Rice Bowl"})
MERGE (d31)-[:BELONGS_TO]->(cat4)
MERGE (d31)-[:HAS_TYPE]->(veg)
MERGE (d31)-[:COSTS]->(p300)
MERGE (d31)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d31)-[:ORIGINATES_FROM]->(c_jap)
WITH d31
MATCH (i1:Ingredient {name: "Kimchi"}), (i2:Ingredient {name: "Basmati Rice"})
MERGE (d31)-[:HAS_INGREDIENT]->(i1)
MERGE (d31)-[:HAS_INGREDIENT]->(i2);

// Dish 32: Sauerkraut Sausage Bowl
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d32:Dish {name: "Sauerkraut Sausage Bowl"})
MERGE (d32)-[:BELONGS_TO]->(cat4)
MERGE (d32)-[:HAS_TYPE]->(nv)
MERGE (d32)-[:COSTS]->(p400)
MERGE (d32)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d32)-[:ORIGINATES_FROM]->(c_spa)
WITH d32
MATCH (i1:Ingredient {name: "Sauerkraut"}), (i2:Ingredient {name: "Beef"})
MERGE (d32)-[:HAS_INGREDIENT]->(i1)
MERGE (d32)-[:HAS_INGREDIENT]->(i2);

// Dish 33: Yogurt Parfait Bowl
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d33:Dish {name: "Yogurt Parfait Bowl"})
MERGE (d33)-[:BELONGS_TO]->(cat4)
MERGE (d33)-[:HAS_TYPE]->(veg)
MERGE (d33)-[:COSTS]->(p200)
MERGE (d33)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d33)-[:ORIGINATES_FROM]->(c_ind)
WITH d33
MATCH (i:Ingredient {name: "Yogurt"})
MERGE (d33)-[:HAS_INGREDIENT]->(i);

// Dish 34: Miso Tofu Bowl
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d34:Dish {name: "Miso Tofu Bowl"})
MERGE (d34)-[:BELONGS_TO]->(cat4)
MERGE (d34)-[:HAS_TYPE]->(veg)
MERGE (d34)-[:COSTS]->(p300)
MERGE (d34)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d34)-[:ORIGINATES_FROM]->(c_jap)
WITH d34
MATCH (i1:Ingredient {name: "Miso"}), (i2:Ingredient {name: "Tofu"})
MERGE (d34)-[:HAS_INGREDIENT]->(i1)
MERGE (d34)-[:HAS_INGREDIENT]->(i2);

// Dish 35: Kimchi Tempeh Bowl
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d35:Dish {name: "Kimchi Tempeh Bowl"})
MERGE (d35)-[:BELONGS_TO]->(cat4)
MERGE (d35)-[:HAS_TYPE]->(veg)
MERGE (d35)-[:COSTS]->(p300)
MERGE (d35)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d35)-[:ORIGINATES_FROM]->(c_jap)
WITH d35
MATCH (i1:Ingredient {name: "Kimchi"}), (i2:Ingredient {name: "Tempeh"})
MERGE (d35)-[:HAS_INGREDIENT]->(i1)
MERGE (d35)-[:HAS_INGREDIENT]->(i2);

// Dish 36: Yogurt Chickpea Curry
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d36:Dish {name: "Yogurt Chickpea Curry"})
MERGE (d36)-[:BELONGS_TO]->(cat4)
MERGE (d36)-[:HAS_TYPE]->(veg)
MERGE (d36)-[:COSTS]->(p300)
MERGE (d36)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d36)-[:ORIGINATES_FROM]->(c_ind)
WITH d36
MATCH (i1:Ingredient {name: "Yogurt"}), (i2:Ingredient {name: "Chickpeas"})
MERGE (d36)-[:HAS_INGREDIENT]->(i1)
MERGE (d36)-[:HAS_INGREDIENT]->(i2);

// Dish 37: Kimchi Fried Rice
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d37:Dish {name: "Kimchi Fried Rice"})
MERGE (d37)-[:BELONGS_TO]->(cat4)
MERGE (d37)-[:HAS_TYPE]->(veg)
MERGE (d37)-[:COSTS]->(p300)
MERGE (d37)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d37)-[:ORIGINATES_FROM]->(c_jap)
WITH d37
MATCH (i1:Ingredient {name: "Kimchi"}), (i2:Ingredient {name: "Basmati Rice"})
MERGE (d37)-[:HAS_INGREDIENT]->(i1)
MERGE (d37)-[:HAS_INGREDIENT]->(i2);

// Dish 38: Miso Soup Classic
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d38:Dish {name: "Miso Soup Classic"})
MERGE (d38)-[:BELONGS_TO]->(cat4)
MERGE (d38)-[:HAS_TYPE]->(veg)
MERGE (d38)-[:COSTS]->(p200)
MERGE (d38)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d38)-[:ORIGINATES_FROM]->(c_jap)
WITH d38
MATCH (i1:Ingredient {name: "Miso"}), (i2:Ingredient {name: "Tofu"})
MERGE (d38)-[:HAS_INGREDIENT]->(i1)
MERGE (d38)-[:HAS_INGREDIENT]->(i2);

// Dish 39: Yogurt Spinach Dip
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d39:Dish {name: "Yogurt Spinach Dip"})
MERGE (d39)-[:BELONGS_TO]->(cat4)
MERGE (d39)-[:HAS_TYPE]->(veg)
MERGE (d39)-[:COSTS]->(p200)
MERGE (d39)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d39)-[:ORIGINATES_FROM]->(c_ind)
WITH d39
MATCH (i1:Ingredient {name: "Yogurt"}), (i2:Ingredient {name: "Spinach"})
MERGE (d39)-[:HAS_INGREDIENT]->(i1)
MERGE (d39)-[:HAS_INGREDIENT]->(i2);

// Dish 40: Sauerkraut Salad
MATCH (cat4:Category {name: "Probiotic & Fermented"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d40:Dish {name: "Sauerkraut Salad"})
MERGE (d40)-[:BELONGS_TO]->(cat4)
MERGE (d40)-[:HAS_TYPE]->(veg)
MERGE (d40)-[:COSTS]->(p200)
MERGE (d40)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d40)-[:ORIGINATES_FROM]->(c_spa)
WITH d40
MATCH (i:Ingredient {name: "Sauerkraut"})
MERGE (d40)-[:HAS_INGREDIENT]->(i);


// ===== CATEGORY 5: Hearty Soups (Dishes 41-50) =====

// Dish 41: Tomato Basil Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d41:Dish {name: "Tomato Basil Soup"})
MERGE (d41)-[:BELONGS_TO]->(cat5)
MERGE (d41)-[:HAS_TYPE]->(veg)
MERGE (d41)-[:COSTS]->(p300)
MERGE (d41)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d41)-[:ORIGINATES_FROM]->(c_ita)
WITH d41
MATCH (i1:Ingredient {name: "Tomato"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d41)-[:HAS_INGREDIENT]->(i1)
MERGE (d41)-[:HAS_INGREDIENT]->(i2);

// Dish 42: Miso Ramen Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d42:Dish {name: "Miso Ramen Soup"})
MERGE (d42)-[:BELONGS_TO]->(cat5)
MERGE (d42)-[:HAS_TYPE]->(nv)
MERGE (d42)-[:COSTS]->(p400)
MERGE (d42)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d42)-[:ORIGINATES_FROM]->(c_jap)
WITH d42
MATCH (i1:Ingredient {name: "Miso"}), (i2:Ingredient {name: "Chicken"})
MERGE (d42)-[:HAS_INGREDIENT]->(i1)
MERGE (d42)-[:HAS_INGREDIENT]->(i2);

// Dish 43: Chickpea Curry Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d43:Dish {name: "Chickpea Curry Soup"})
MERGE (d43)-[:BELONGS_TO]->(cat5)
MERGE (d43)-[:HAS_TYPE]->(veg)
MERGE (d43)-[:COSTS]->(p300)
MERGE (d43)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d43)-[:ORIGINATES_FROM]->(c_ind)
WITH d43
MATCH (i1:Ingredient {name: "Chickpeas"}), (i2:Ingredient {name: "Turmeric"})
MERGE (d43)-[:HAS_INGREDIENT]->(i1)
MERGE (d43)-[:HAS_INGREDIENT]->(i2);

// Dish 44: Black Bean Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d44:Dish {name: "Black Bean Soup"})
MERGE (d44)-[:BELONGS_TO]->(cat5)
MERGE (d44)-[:HAS_TYPE]->(veg)
MERGE (d44)-[:COSTS]->(p300)
MERGE (d44)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d44)-[:ORIGINATES_FROM]->(c_mex)
WITH d44
MATCH (i1:Ingredient {name: "Black Beans"}), (i2:Ingredient {name: "Corn"})
MERGE (d44)-[:HAS_INGREDIENT]->(i1)
MERGE (d44)-[:HAS_INGREDIENT]->(i2);

// Dish 45: Saffron Seafood Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d45:Dish {name: "Saffron Seafood Soup"})
MERGE (d45)-[:BELONGS_TO]->(cat5)
MERGE (d45)-[:HAS_TYPE]->(nv)
MERGE (d45)-[:COSTS]->(p500)
MERGE (d45)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d45)-[:ORIGINATES_FROM]->(c_spa)
WITH d45
MATCH (i1:Ingredient {name: "Saffron"}), (i2:Ingredient {name: "Shrimp"})
MERGE (d45)-[:HAS_INGREDIENT]->(i1)
MERGE (d45)-[:HAS_INGREDIENT]->(i2);

// Dish 46: Lemon Chicken Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d46:Dish {name: "Lemon Chicken Soup"})
MERGE (d46)-[:BELONGS_TO]->(cat5)
MERGE (d46)-[:HAS_TYPE]->(nv)
MERGE (d46)-[:COSTS]->(p400)
MERGE (d46)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d46)-[:ORIGINATES_FROM]->(c_ind)
WITH d46
MATCH (i1:Ingredient {name: "Lemon"}), (i2:Ingredient {name: "Chicken"})
MERGE (d46)-[:HAS_INGREDIENT]->(i1)
MERGE (d46)-[:HAS_INGREDIENT]->(i2);

// Dish 47: Pasta Minestrone
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d47:Dish {name: "Pasta Minestrone"})
MERGE (d47)-[:BELONGS_TO]->(cat5)
MERGE (d47)-[:HAS_TYPE]->(veg)
MERGE (d47)-[:COSTS]->(p300)
MERGE (d47)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d47)-[:ORIGINATES_FROM]->(c_ita)
WITH d47
MATCH (i1:Ingredient {name: "Pasta"}), (i2:Ingredient {name: "Tomato"})
MERGE (d47)-[:HAS_INGREDIENT]->(i1)
MERGE (d47)-[:HAS_INGREDIENT]->(i2);

// Dish 48: Tofu Miso Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d48:Dish {name: "Tofu Miso Soup"})
MERGE (d48)-[:BELONGS_TO]->(cat5)
MERGE (d48)-[:HAS_TYPE]->(veg)
MERGE (d48)-[:COSTS]->(p300)
MERGE (d48)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d48)-[:ORIGINATES_FROM]->(c_jap)
WITH d48
MATCH (i1:Ingredient {name: "Tofu"}), (i2:Ingredient {name: "Miso"})
MERGE (d48)-[:HAS_INGREDIENT]->(i1)
MERGE (d48)-[:HAS_INGREDIENT]->(i2);

// Dish 49: Spinach Lentil Soup
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d49:Dish {name: "Spinach Lentil Soup"})
MERGE (d49)-[:BELONGS_TO]->(cat5)
MERGE (d49)-[:HAS_TYPE]->(veg)
MERGE (d49)-[:COSTS]->(p300)
MERGE (d49)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d49)-[:ORIGINATES_FROM]->(c_ind)
WITH d49
MATCH (i1:Ingredient {name: "Spinach"}), (i2:Ingredient {name: "Turmeric"})
MERGE (d49)-[:HAS_INGREDIENT]->(i1)
MERGE (d49)-[:HAS_INGREDIENT]->(i2);

// Dish 50: Corn Chowder
MATCH (cat5:Category {name: "Hearty Soups"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d50:Dish {name: "Corn Chowder"})
MERGE (d50)-[:BELONGS_TO]->(cat5)
MERGE (d50)-[:HAS_TYPE]->(veg)
MERGE (d50)-[:COSTS]->(p300)
MERGE (d50)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d50)-[:ORIGINATES_FROM]->(c_mex)
WITH d50
MATCH (i:Ingredient {name: "Corn"})
MERGE (d50)-[:HAS_INGREDIENT]->(i);


// ===== CATEGORY 6: Quick Bites (Dishes 51-60) =====

// Dish 51: Paneer Tikka Wrap
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d51:Dish {name: "Paneer Tikka Wrap"})
MERGE (d51)-[:BELONGS_TO]->(cat6)
MERGE (d51)-[:HAS_TYPE]->(veg)
MERGE (d51)-[:COSTS]->(p300)
MERGE (d51)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d51)-[:ORIGINATES_FROM]->(c_ind)
WITH d51
MATCH (i:Ingredient {name: "Paneer"})
MERGE (d51)-[:HAS_INGREDIENT]->(i);

// Dish 52: Chicken Taco
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (nv:Type {name: "Non-Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d52:Dish {name: "Chicken Taco"})
MERGE (d52)-[:BELONGS_TO]->(cat6)
MERGE (d52)-[:HAS_TYPE]->(nv)
MERGE (d52)-[:COSTS]->(p300)
MERGE (d52)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d52)-[:ORIGINATES_FROM]->(c_mex)
WITH d52
MATCH (i1:Ingredient {name: "Chicken"}), (i2:Ingredient {name: "Corn"})
MERGE (d52)-[:HAS_INGREDIENT]->(i1)
MERGE (d52)-[:HAS_INGREDIENT]->(i2);

// Dish 53: Avocado Toast
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d53:Dish {name: "Avocado Toast"})
MERGE (d53)-[:BELONGS_TO]->(cat6)
MERGE (d53)-[:HAS_TYPE]->(veg)
MERGE (d53)-[:COSTS]->(p200)
MERGE (d53)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d53)-[:ORIGINATES_FROM]->(c_mex)
WITH d53
MATCH (i:Ingredient {name: "Avocado"})
MERGE (d53)-[:HAS_INGREDIENT]->(i);

// Dish 54: Salmon Sushi Roll
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d54:Dish {name: "Salmon Sushi Roll"})
MERGE (d54)-[:BELONGS_TO]->(cat6)
MERGE (d54)-[:HAS_TYPE]->(nv)
MERGE (d54)-[:COSTS]->(p400)
MERGE (d54)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d54)-[:ORIGINATES_FROM]->(c_jap)
WITH d54
MATCH (i1:Ingredient {name: "Salmon"}), (i2:Ingredient {name: "Seaweed"})
MERGE (d54)-[:HAS_INGREDIENT]->(i1)
MERGE (d54)-[:HAS_INGREDIENT]->(i2);

// Dish 55: Tomato Bruschetta
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d55:Dish {name: "Tomato Bruschetta"})
MERGE (d55)-[:BELONGS_TO]->(cat6)
MERGE (d55)-[:HAS_TYPE]->(veg)
MERGE (d55)-[:COSTS]->(p200)
MERGE (d55)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d55)-[:ORIGINATES_FROM]->(c_ita)
WITH d55
MATCH (i1:Ingredient {name: "Tomato"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d55)-[:HAS_INGREDIENT]->(i1)
MERGE (d55)-[:HAS_INGREDIENT]->(i2);

// Dish 56: Beef Quesadilla
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (nv:Type {name: "Non-Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d56:Dish {name: "Beef Quesadilla"})
MERGE (d56)-[:BELONGS_TO]->(cat6)
MERGE (d56)-[:HAS_TYPE]->(nv)
MERGE (d56)-[:COSTS]->(p300)
MERGE (d56)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d56)-[:ORIGINATES_FROM]->(c_mex)
WITH d56
MATCH (i1:Ingredient {name: "Beef"}), (i2:Ingredient {name: "Jalapenos"})
MERGE (d56)-[:HAS_INGREDIENT]->(i1)
MERGE (d56)-[:HAS_INGREDIENT]->(i2);

// Dish 57: Tofu Spring Roll
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d57:Dish {name: "Tofu Spring Roll"})
MERGE (d57)-[:BELONGS_TO]->(cat6)
MERGE (d57)-[:HAS_TYPE]->(veg)
MERGE (d57)-[:COSTS]->(p200)
MERGE (d57)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d57)-[:ORIGINATES_FROM]->(c_jap)
WITH d57
MATCH (i:Ingredient {name: "Tofu"})
MERGE (d57)-[:HAS_INGREDIENT]->(i);

// Dish 58: Shrimp Tapas
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d58:Dish {name: "Shrimp Tapas"})
MERGE (d58)-[:BELONGS_TO]->(cat6)
MERGE (d58)-[:HAS_TYPE]->(nv)
MERGE (d58)-[:COSTS]->(p400)
MERGE (d58)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d58)-[:ORIGINATES_FROM]->(c_spa)
WITH d58
MATCH (i1:Ingredient {name: "Shrimp"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d58)-[:HAS_INGREDIENT]->(i1)
MERGE (d58)-[:HAS_INGREDIENT]->(i2);

// Dish 59: Chickpea Falafel
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d59:Dish {name: "Chickpea Falafel"})
MERGE (d59)-[:BELONGS_TO]->(cat6)
MERGE (d59)-[:HAS_TYPE]->(veg)
MERGE (d59)-[:COSTS]->(p200)
MERGE (d59)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d59)-[:ORIGINATES_FROM]->(c_ind)
WITH d59
MATCH (i:Ingredient {name: "Chickpeas"})
MERGE (d59)-[:HAS_INGREDIENT]->(i);

// Dish 60: Tempeh Lettuce Wrap
MATCH (cat6:Category {name: "Quick Bites"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d60:Dish {name: "Tempeh Lettuce Wrap"})
MERGE (d60)-[:BELONGS_TO]->(cat6)
MERGE (d60)-[:HAS_TYPE]->(veg)
MERGE (d60)-[:COSTS]->(p200)
MERGE (d60)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d60)-[:ORIGINATES_FROM]->(c_jap)
WITH d60
MATCH (i1:Ingredient {name: "Tempeh"}), (i2:Ingredient {name: "Spinach"})
MERGE (d60)-[:HAS_INGREDIENT]->(i1)
MERGE (d60)-[:HAS_INGREDIENT]->(i2);


// ===== CATEGORY 7: Hydration & Drinks (Dishes 61-70) =====

// Dish 61: Lemon Water Detox
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d61:Dish {name: "Lemon Water Detox"})
MERGE (d61)-[:BELONGS_TO]->(cat7)
MERGE (d61)-[:HAS_TYPE]->(veg)
MERGE (d61)-[:COSTS]->(p200)
MERGE (d61)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d61)-[:ORIGINATES_FROM]->(c_ind)
WITH d61
MATCH (i:Ingredient {name: "Lemon"})
MERGE (d61)-[:HAS_INGREDIENT]->(i);

// Dish 62: Mango Yogurt Smoothie
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d62:Dish {name: "Mango Yogurt Smoothie"})
MERGE (d62)-[:BELONGS_TO]->(cat7)
MERGE (d62)-[:HAS_TYPE]->(veg)
MERGE (d62)-[:COSTS]->(p300)
MERGE (d62)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d62)-[:ORIGINATES_FROM]->(c_ind)
WITH d62
MATCH (i:Ingredient {name: "Yogurt"})
MERGE (d62)-[:HAS_INGREDIENT]->(i);

// Dish 63: Kale Green Smoothie
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d63:Dish {name: "Kale Green Smoothie"})
MERGE (d63)-[:BELONGS_TO]->(cat7)
MERGE (d63)-[:HAS_TYPE]->(veg)
MERGE (d63)-[:COSTS]->(p300)
MERGE (d63)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d63)-[:ORIGINATES_FROM]->(c_mex)
WITH d63
MATCH (i1:Ingredient {name: "Kale"}), (i2:Ingredient {name: "Avocado"})
MERGE (d63)-[:HAS_INGREDIENT]->(i1)
MERGE (d63)-[:HAS_INGREDIENT]->(i2);

// Dish 64: Tomato Juice Fresh
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d64:Dish {name: "Tomato Juice Fresh"})
MERGE (d64)-[:BELONGS_TO]->(cat7)
MERGE (d64)-[:HAS_TYPE]->(veg)
MERGE (d64)-[:COSTS]->(p200)
MERGE (d64)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d64)-[:ORIGINATES_FROM]->(c_ita)
WITH d64
MATCH (i:Ingredient {name: "Tomato"})
MERGE (d64)-[:HAS_INGREDIENT]->(i);

// Dish 65: Spinach Protein Shake
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d65:Dish {name: "Spinach Protein Shake"})
MERGE (d65)-[:BELONGS_TO]->(cat7)
MERGE (d65)-[:HAS_TYPE]->(veg)
MERGE (d65)-[:COSTS]->(p300)
MERGE (d65)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d65)-[:ORIGINATES_FROM]->(c_ind)
WITH d65
MATCH (i1:Ingredient {name: "Spinach"}), (i2:Ingredient {name: "Yogurt"})
MERGE (d65)-[:HAS_INGREDIENT]->(i1)
MERGE (d65)-[:HAS_INGREDIENT]->(i2);

// Dish 66: Lemon Mint Cooler
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d66:Dish {name: "Lemon Mint Cooler"})
MERGE (d66)-[:BELONGS_TO]->(cat7)
MERGE (d66)-[:HAS_TYPE]->(veg)
MERGE (d66)-[:COSTS]->(p200)
MERGE (d66)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d66)-[:ORIGINATES_FROM]->(c_spa)
WITH d66
MATCH (i:Ingredient {name: "Lemon"})
MERGE (d66)-[:HAS_INGREDIENT]->(i);

// Dish 67: Avocado Smoothie
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d67:Dish {name: "Avocado Smoothie"})
MERGE (d67)-[:BELONGS_TO]->(cat7)
MERGE (d67)-[:HAS_TYPE]->(veg)
MERGE (d67)-[:COSTS]->(p300)
MERGE (d67)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d67)-[:ORIGINATES_FROM]->(c_mex)
WITH d67
MATCH (i:Ingredient {name: "Avocado"})
MERGE (d67)-[:HAS_INGREDIENT]->(i);

// Dish 68: Turmeric Golden Milk
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d68:Dish {name: "Turmeric Golden Milk"})
MERGE (d68)-[:BELONGS_TO]->(cat7)
MERGE (d68)-[:HAS_TYPE]->(veg)
MERGE (d68)-[:COSTS]->(p200)
MERGE (d68)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d68)-[:ORIGINATES_FROM]->(c_ind)
WITH d68
MATCH (i:Ingredient {name: "Turmeric"})
MERGE (d68)-[:HAS_INGREDIENT]->(i);

// Dish 69: Corn Milk Shake
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d69:Dish {name: "Corn Milk Shake"})
MERGE (d69)-[:BELONGS_TO]->(cat7)
MERGE (d69)-[:HAS_TYPE]->(veg)
MERGE (d69)-[:COSTS]->(p200)
MERGE (d69)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d69)-[:ORIGINATES_FROM]->(c_mex)
WITH d69
MATCH (i:Ingredient {name: "Corn"})
MERGE (d69)-[:HAS_INGREDIENT]->(i);

// Dish 70: Walnut Date Shake
MATCH (cat7:Category {name: "Hydration & Drinks"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d70:Dish {name: "Walnut Date Shake"})
MERGE (d70)-[:BELONGS_TO]->(cat7)
MERGE (d70)-[:HAS_TYPE]->(veg)
MERGE (d70)-[:COSTS]->(p300)
MERGE (d70)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d70)-[:ORIGINATES_FROM]->(c_spa)
WITH d70
MATCH (i:Ingredient {name: "Walnuts"})
MERGE (d70)-[:HAS_INGREDIENT]->(i);


// ===== CATEGORY 8: Plant-Based (Dishes 71-80) =====

// Dish 71: Quinoa Buddha Bowl
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d71:Dish {name: "Quinoa Buddha Bowl"})
MERGE (d71)-[:BELONGS_TO]->(cat8)
MERGE (d71)-[:HAS_TYPE]->(veg)
MERGE (d71)-[:COSTS]->(p300)
MERGE (d71)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d71)-[:ORIGINATES_FROM]->(c_ind)
WITH d71
MATCH (i:Ingredient {name: "Quinoa"})
MERGE (d71)-[:HAS_INGREDIENT]->(i);

// Dish 72: Tofu Stir Fry
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d72:Dish {name: "Tofu Stir Fry"})
MERGE (d72)-[:BELONGS_TO]->(cat8)
MERGE (d72)-[:HAS_TYPE]->(veg)
MERGE (d72)-[:COSTS]->(p300)
MERGE (d72)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d72)-[:ORIGINATES_FROM]->(c_jap)
WITH d72
MATCH (i:Ingredient {name: "Tofu"})
MERGE (d72)-[:HAS_INGREDIENT]->(i);

// Dish 73: Tempeh Power Bowl
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d73:Dish {name: "Tempeh Power Bowl"})
MERGE (d73)-[:BELONGS_TO]->(cat8)
MERGE (d73)-[:HAS_TYPE]->(veg)
MERGE (d73)-[:COSTS]->(p300)
MERGE (d73)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d73)-[:ORIGINATES_FROM]->(c_jap)
WITH d73
MATCH (i:Ingredient {name: "Tempeh"})
MERGE (d73)-[:HAS_INGREDIENT]->(i);

// Dish 74: Chickpea Masala
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d74:Dish {name: "Chickpea Masala"})
MERGE (d74)-[:BELONGS_TO]->(cat8)
MERGE (d74)-[:HAS_TYPE]->(veg)
MERGE (d74)-[:COSTS]->(p300)
MERGE (d74)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d74)-[:ORIGINATES_FROM]->(c_ind)
WITH d74
MATCH (i1:Ingredient {name: "Chickpeas"}), (i2:Ingredient {name: "Turmeric"})
MERGE (d74)-[:HAS_INGREDIENT]->(i1)
MERGE (d74)-[:HAS_INGREDIENT]->(i2);

// Dish 75: Black Bean Burrito Bowl
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d75:Dish {name: "Black Bean Burrito Bowl"})
MERGE (d75)-[:BELONGS_TO]->(cat8)
MERGE (d75)-[:HAS_TYPE]->(veg)
MERGE (d75)-[:COSTS]->(p300)
MERGE (d75)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d75)-[:ORIGINATES_FROM]->(c_mex)
WITH d75
MATCH (i1:Ingredient {name: "Black Beans"}), (i2:Ingredient {name: "Avocado"})
MERGE (d75)-[:HAS_INGREDIENT]->(i1)
MERGE (d75)-[:HAS_INGREDIENT]->(i2);

// Dish 76: Kale Quinoa Salad
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d76:Dish {name: "Kale Quinoa Salad"})
MERGE (d76)-[:BELONGS_TO]->(cat8)
MERGE (d76)-[:HAS_TYPE]->(veg)
MERGE (d76)-[:COSTS]->(p300)
MERGE (d76)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d76)-[:ORIGINATES_FROM]->(c_ita)
WITH d76
MATCH (i1:Ingredient {name: "Kale"}), (i2:Ingredient {name: "Quinoa"})
MERGE (d76)-[:HAS_INGREDIENT]->(i1)
MERGE (d76)-[:HAS_INGREDIENT]->(i2);

// Dish 77: Spinach Tofu Curry
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d77:Dish {name: "Spinach Tofu Curry"})
MERGE (d77)-[:BELONGS_TO]->(cat8)
MERGE (d77)-[:HAS_TYPE]->(veg)
MERGE (d77)-[:COSTS]->(p300)
MERGE (d77)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d77)-[:ORIGINATES_FROM]->(c_ind)
WITH d77
MATCH (i1:Ingredient {name: "Spinach"}), (i2:Ingredient {name: "Tofu"})
MERGE (d77)-[:HAS_INGREDIENT]->(i1)
MERGE (d77)-[:HAS_INGREDIENT]->(i2);

// Dish 78: Arugula Walnut Bowl
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d78:Dish {name: "Arugula Walnut Bowl"})
MERGE (d78)-[:BELONGS_TO]->(cat8)
MERGE (d78)-[:HAS_TYPE]->(veg)
MERGE (d78)-[:COSTS]->(p300)
MERGE (d78)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d78)-[:ORIGINATES_FROM]->(c_ita)
WITH d78
MATCH (i1:Ingredient {name: "Arugula"}), (i2:Ingredient {name: "Walnuts"})
MERGE (d78)-[:HAS_INGREDIENT]->(i1)
MERGE (d78)-[:HAS_INGREDIENT]->(i2);

// Dish 79: Seaweed Tempeh Bowl
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d79:Dish {name: "Seaweed Tempeh Bowl"})
MERGE (d79)-[:BELONGS_TO]->(cat8)
MERGE (d79)-[:HAS_TYPE]->(veg)
MERGE (d79)-[:COSTS]->(p300)
MERGE (d79)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d79)-[:ORIGINATES_FROM]->(c_jap)
WITH d79
MATCH (i1:Ingredient {name: "Seaweed"}), (i2:Ingredient {name: "Tempeh"})
MERGE (d79)-[:HAS_INGREDIENT]->(i1)
MERGE (d79)-[:HAS_INGREDIENT]->(i2);

// Dish 80: Lemon Chickpea Stew
MATCH (cat8:Category {name: "Plant-Based"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d80:Dish {name: "Lemon Chickpea Stew"})
MERGE (d80)-[:BELONGS_TO]->(cat8)
MERGE (d80)-[:HAS_TYPE]->(veg)
MERGE (d80)-[:COSTS]->(p300)
MERGE (d80)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d80)-[:ORIGINATES_FROM]->(c_spa)
WITH d80
MATCH (i1:Ingredient {name: "Lemon"}), (i2:Ingredient {name: "Chickpeas"})
MERGE (d80)-[:HAS_INGREDIENT]->(i1)
MERGE (d80)-[:HAS_INGREDIENT]->(i2);


// ===== CATEGORY 9: Keto-Friendly (Dishes 81-90) =====

// Dish 81: Keto Salmon Plate
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d81:Dish {name: "Keto Salmon Plate"})
MERGE (d81)-[:BELONGS_TO]->(cat9)
MERGE (d81)-[:HAS_TYPE]->(nv)
MERGE (d81)-[:COSTS]->(p500)
MERGE (d81)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d81)-[:ORIGINATES_FROM]->(c_jap)
WITH d81
MATCH (i1:Ingredient {name: "Salmon"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d81)-[:HAS_INGREDIENT]->(i1)
MERGE (d81)-[:HAS_INGREDIENT]->(i2);

// Dish 82: Keto Chicken Bowl
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (nv:Type {name: "Non-Veg"}), (p400:Price {value: 400})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d82:Dish {name: "Keto Chicken Bowl"})
MERGE (d82)-[:BELONGS_TO]->(cat9)
MERGE (d82)-[:HAS_TYPE]->(nv)
MERGE (d82)-[:COSTS]->(p400)
MERGE (d82)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d82)-[:ORIGINATES_FROM]->(c_ind)
WITH d82
MATCH (i1:Ingredient {name: "Chicken"}), (i2:Ingredient {name: "Spinach"})
MERGE (d82)-[:HAS_INGREDIENT]->(i1)
MERGE (d82)-[:HAS_INGREDIENT]->(i2);

// Dish 83: Keto Beef Platter
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d83:Dish {name: "Keto Beef Platter"})
MERGE (d83)-[:BELONGS_TO]->(cat9)
MERGE (d83)-[:HAS_TYPE]->(nv)
MERGE (d83)-[:COSTS]->(p500)
MERGE (d83)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d83)-[:ORIGINATES_FROM]->(c_mex)
WITH d83
MATCH (i1:Ingredient {name: "Beef"}), (i2:Ingredient {name: "Avocado"})
MERGE (d83)-[:HAS_INGREDIENT]->(i1)
MERGE (d83)-[:HAS_INGREDIENT]->(i2);

// Dish 84: Keto Shrimp Delight
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (nv:Type {name: "Non-Veg"}), (p500:Price {value: 500})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d84:Dish {name: "Keto Shrimp Delight"})
MERGE (d84)-[:BELONGS_TO]->(cat9)
MERGE (d84)-[:HAS_TYPE]->(nv)
MERGE (d84)-[:COSTS]->(p500)
MERGE (d84)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d84)-[:ORIGINATES_FROM]->(c_spa)
WITH d84
MATCH (i1:Ingredient {name: "Shrimp"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d84)-[:HAS_INGREDIENT]->(i1)
MERGE (d84)-[:HAS_INGREDIENT]->(i2);

// Dish 85: Keto Paneer Tikka
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d85:Dish {name: "Keto Paneer Tikka"})
MERGE (d85)-[:BELONGS_TO]->(cat9)
MERGE (d85)-[:HAS_TYPE]->(veg)
MERGE (d85)-[:COSTS]->(p300)
MERGE (d85)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d85)-[:ORIGINATES_FROM]->(c_ind)
WITH d85
MATCH (i1:Ingredient {name: "Paneer"}), (i2:Ingredient {name: "Spinach"})
MERGE (d85)-[:HAS_INGREDIENT]->(i1)
MERGE (d85)-[:HAS_INGREDIENT]->(i2);

// Dish 86: Keto Tofu Scramble
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d86:Dish {name: "Keto Tofu Scramble"})
MERGE (d86)-[:BELONGS_TO]->(cat9)
MERGE (d86)-[:HAS_TYPE]->(veg)
MERGE (d86)-[:COSTS]->(p300)
MERGE (d86)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d86)-[:ORIGINATES_FROM]->(c_jap)
WITH d86
MATCH (i1:Ingredient {name: "Tofu"}), (i2:Ingredient {name: "Kale"})
MERGE (d86)-[:HAS_INGREDIENT]->(i1)
MERGE (d86)-[:HAS_INGREDIENT]->(i2);

// Dish 87: Keto Arugula Salad
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d87:Dish {name: "Keto Arugula Salad"})
MERGE (d87)-[:BELONGS_TO]->(cat9)
MERGE (d87)-[:HAS_TYPE]->(veg)
MERGE (d87)-[:COSTS]->(p300)
MERGE (d87)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d87)-[:ORIGINATES_FROM]->(c_ita)
WITH d87
MATCH (i1:Ingredient {name: "Arugula"}), (i2:Ingredient {name: "Walnuts"})
MERGE (d87)-[:HAS_INGREDIENT]->(i1)
MERGE (d87)-[:HAS_INGREDIENT]->(i2);

// Dish 88: Keto Avocado Bowl
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d88:Dish {name: "Keto Avocado Bowl"})
MERGE (d88)-[:BELONGS_TO]->(cat9)
MERGE (d88)-[:HAS_TYPE]->(veg)
MERGE (d88)-[:COSTS]->(p300)
MERGE (d88)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d88)-[:ORIGINATES_FROM]->(c_mex)
WITH d88
MATCH (i1:Ingredient {name: "Avocado"}), (i2:Ingredient {name: "Spinach"})
MERGE (d88)-[:HAS_INGREDIENT]->(i1)
MERGE (d88)-[:HAS_INGREDIENT]->(i2);

// Dish 89: Keto Seaweed Snack
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d89:Dish {name: "Keto Seaweed Snack"})
MERGE (d89)-[:BELONGS_TO]->(cat9)
MERGE (d89)-[:HAS_TYPE]->(veg)
MERGE (d89)-[:COSTS]->(p200)
MERGE (d89)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d89)-[:ORIGINATES_FROM]->(c_jap)
WITH d89
MATCH (i:Ingredient {name: "Seaweed"})
MERGE (d89)-[:HAS_INGREDIENT]->(i);

// Dish 90: Keto Feta Spinach
MATCH (cat9:Category {name: "Keto-Friendly"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d90:Dish {name: "Keto Feta Spinach"})
MERGE (d90)-[:BELONGS_TO]->(cat9)
MERGE (d90)-[:HAS_TYPE]->(veg)
MERGE (d90)-[:COSTS]->(p300)
MERGE (d90)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d90)-[:ORIGINATES_FROM]->(c_spa)
WITH d90
MATCH (i1:Ingredient {name: "Feta Cheese"}), (i2:Ingredient {name: "Spinach"})
MERGE (d90)-[:HAS_INGREDIENT]->(i1)
MERGE (d90)-[:HAS_INGREDIENT]->(i2);


// ===== CATEGORY 10: Guilt-Free Treats (Dishes 91-100) =====

// Dish 91: Yogurt Berry Parfait
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d91:Dish {name: "Yogurt Berry Parfait"})
MERGE (d91)-[:BELONGS_TO]->(cat10)
MERGE (d91)-[:HAS_TYPE]->(veg)
MERGE (d91)-[:COSTS]->(p200)
MERGE (d91)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d91)-[:ORIGINATES_FROM]->(c_ind)
WITH d91
MATCH (i:Ingredient {name: "Yogurt"})
MERGE (d91)-[:HAS_INGREDIENT]->(i);

// Dish 92: Avocado Chocolate Mousse
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_mex:Cuisine {name: "Mexican"})
MERGE (d92:Dish {name: "Avocado Chocolate Mousse"})
MERGE (d92)-[:BELONGS_TO]->(cat10)
MERGE (d92)-[:HAS_TYPE]->(veg)
MERGE (d92)-[:COSTS]->(p300)
MERGE (d92)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d92)-[:ORIGINATES_FROM]->(c_mex)
WITH d92
MATCH (i:Ingredient {name: "Avocado"})
MERGE (d92)-[:HAS_INGREDIENT]->(i);

// Dish 93: Tofu Cheesecake
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p300:Price {value: 300})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d93:Dish {name: "Tofu Cheesecake"})
MERGE (d93)-[:BELONGS_TO]->(cat10)
MERGE (d93)-[:HAS_TYPE]->(veg)
MERGE (d93)-[:COSTS]->(p300)
MERGE (d93)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d93)-[:ORIGINATES_FROM]->(c_jap)
WITH d93
MATCH (i:Ingredient {name: "Tofu"})
MERGE (d93)-[:HAS_INGREDIENT]->(i);

// Dish 94: Walnut Energy Bites
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d94:Dish {name: "Walnut Energy Bites"})
MERGE (d94)-[:BELONGS_TO]->(cat10)
MERGE (d94)-[:HAS_TYPE]->(veg)
MERGE (d94)-[:COSTS]->(p200)
MERGE (d94)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d94)-[:ORIGINATES_FROM]->(c_spa)
WITH d94
MATCH (i:Ingredient {name: "Walnuts"})
MERGE (d94)-[:HAS_INGREDIENT]->(i);

// Dish 95: Quinoa Pudding
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d95:Dish {name: "Quinoa Pudding"})
MERGE (d95)-[:BELONGS_TO]->(cat10)
MERGE (d95)-[:HAS_TYPE]->(veg)
MERGE (d95)-[:COSTS]->(p200)
MERGE (d95)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d95)-[:ORIGINATES_FROM]->(c_ind)
WITH d95
MATCH (i:Ingredient {name: "Quinoa"})
MERGE (d95)-[:HAS_INGREDIENT]->(i);

// Dish 96: Lemon Chia Pudding
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nAntiox:Nutrition {label: "Antioxidant Rich"}), (c_spa:Cuisine {name: "Spanish"})
MERGE (d96:Dish {name: "Lemon Chia Pudding"})
MERGE (d96)-[:BELONGS_TO]->(cat10)
MERGE (d96)-[:HAS_TYPE]->(veg)
MERGE (d96)-[:COSTS]->(p200)
MERGE (d96)-[:NUTRITIONAL_BENEFIT]->(nAntiox)
MERGE (d96)-[:ORIGINATES_FROM]->(c_spa)
WITH d96
MATCH (i:Ingredient {name: "Lemon"})
MERGE (d96)-[:HAS_INGREDIENT]->(i);

// Dish 97: Chickpea Cookie Dough
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d97:Dish {name: "Chickpea Cookie Dough"})
MERGE (d97)-[:BELONGS_TO]->(cat10)
MERGE (d97)-[:HAS_TYPE]->(veg)
MERGE (d97)-[:COSTS]->(p200)
MERGE (d97)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d97)-[:ORIGINATES_FROM]->(c_ind)
WITH d97
MATCH (i:Ingredient {name: "Chickpeas"})
MERGE (d97)-[:HAS_INGREDIENT]->(i);

// Dish 98: Yogurt Popsicles
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_ind:Cuisine {name: "Indian"})
MERGE (d98:Dish {name: "Yogurt Popsicles"})
MERGE (d98)-[:BELONGS_TO]->(cat10)
MERGE (d98)-[:HAS_TYPE]->(veg)
MERGE (d98)-[:COSTS]->(p200)
MERGE (d98)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d98)-[:ORIGINATES_FROM]->(c_ind)
WITH d98
MATCH (i:Ingredient {name: "Yogurt"})
MERGE (d98)-[:HAS_INGREDIENT]->(i);

// Dish 99: Kale Chips
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nFiber:Nutrition {label: "High Fiber"}), (c_ita:Cuisine {name: "Italian"})
MERGE (d99:Dish {name: "Kale Chips"})
MERGE (d99)-[:BELONGS_TO]->(cat10)
MERGE (d99)-[:HAS_TYPE]->(veg)
MERGE (d99)-[:COSTS]->(p200)
MERGE (d99)-[:NUTRITIONAL_BENEFIT]->(nFiber)
MERGE (d99)-[:ORIGINATES_FROM]->(c_ita)
WITH d99
MATCH (i1:Ingredient {name: "Kale"}), (i2:Ingredient {name: "Olive Oil"})
MERGE (d99)-[:HAS_INGREDIENT]->(i1)
MERGE (d99)-[:HAS_INGREDIENT]->(i2);

// Dish 100: Tempeh Sweet Bites
MATCH (cat10:Category {name: "Guilt-Free Treats"})
MATCH (veg:Type {name: "Veg"}), (p200:Price {value: 200})
MATCH (nProt:Nutrition {label: "High Protein"}), (c_jap:Cuisine {name: "Japanese"})
MERGE (d100:Dish {name: "Tempeh Sweet Bites"})
MERGE (d100)-[:BELONGS_TO]->(cat10)
MERGE (d100)-[:HAS_TYPE]->(veg)
MERGE (d100)-[:COSTS]->(p200)
MERGE (d100)-[:NUTRITIONAL_BENEFIT]->(nProt)
MERGE (d100)-[:ORIGINATES_FROM]->(c_jap)
WITH d100
MATCH (i:Ingredient {name: "Tempeh"})
MERGE (d100)-[:HAS_INGREDIENT]->(i);