
import bevezetes
import sorozat
import epuletek


# Feladat 1.
nev, szerepkor, elet = bevezetes.Bekeres()


print(f"\nI/A:\n\tJátékos neve: {nev}\n\tszerepkör: {szerepkor}")
print(f"\nI/B:\n\tÜdvözlünk {nev}, {elet} életed van!")








# Feladat 2.
print(f"\nII/A, B, C:\n")
sorozat.konzol_kiir()

db = sorozat.fejek_szama()
print(f"\n\nII/D, E:\n\n\tA fejek száma: {db}.")

sorozat.file_kiir()








# Feladat 3.
szam1 = epuletek.EpuletSzamolas()
print(f"\nIII/A, B:\n\tAz épületek száma: {szam1}")


szam2 = epuletek.MagasEpuletek()
print(f"III/C:\n\tAz 555 lábnál magasabb épületek száma: {szam2}.")


epulet = epuletek.LegoregebbEpulet()
print(f"III/D:\n\tA legöregebb épület országa: {epulet}.")















