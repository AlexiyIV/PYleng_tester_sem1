#Напишите программу для проверки ложности утверждения
#(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.
for w in[True, False]:
    for x in[True, False]:
        for y in[True, False]:
            for z in[True, False]:
                print('(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) = ', ((w and z) or (not y) or ((not x) == (not w))))
