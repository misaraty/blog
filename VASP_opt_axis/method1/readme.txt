ISIF=3
对于其他方向晶格基矢的修改同理：对于a方向基矢，将 FCELL(3,I) 和 FCELL(I,3) 分别改为 FCELL(1,I) 和 FCELL(I,1) ；对于b方向基矢，则分别改为 FCELL(2,I) 和 FCELL(I,2) ；固定两个基矢则应该同时将两个方向对应的矩阵元设置为0。

cite: https://zhuanlan.zhihu.com/p/34750103