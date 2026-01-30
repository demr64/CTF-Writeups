The first room is obviously just rot13 cipher, we can solve it through
cyberchef or a script:
```
ZHOFRPH WR WKH ILUVW FKDPEHU
           
WELCOME TO THE FIRST CHAMBER
```
The second room, it's a simple substitution cipher, we can use quipqiup to bruteforce it:
```
QVE KEICAY JCCD JEMZLJEK BOQLEAIE

THE SECOND ROOM REQUIRES PATIENCE
```

The third is trickier. It's in hex format, so we decode it, we obtain an unprintable text. But we know that the flag starts with 'JDHACK', therefore we can try using XOR, obtaining 'VIDEO', then it becomes clear it's just a repeating-key XOR cipher, we obtain:
```
1c0d0c040c1d3207710a057d161a18621a1b0410117d09761d2b

JDHACK{C4ES4R_W4S_A_G4M3R}
```
