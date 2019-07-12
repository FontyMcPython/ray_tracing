# 2D Ray tracing tests
My goal is to play around with 2D graphics. The project is completely open so feel free to contribute.

## Ray collision
![scheme](https://github.com/FontyMcPython/ray_tracing/blob/master/scheme.png)

Two elements interact when it comes to the collision of the rays. In the first place the walls, which are defined by two points, _A_ and _B_. On the other hand, the rays themselves are defined by a point, _C_, and the angle _α_. Both can be expressed in the parametric form by adding the parameters _r1_ and _r2_. The collision point, if it exists, is labeled _X_.

Wall:

```
X = A + r2*(B-A)
0 <= r2 <= 1
```

Ray:

```
X = C + r1*(cos(α), sin(α))
0 <= r1
```

With some basic operation, _r2_ can be reduced to:

```  
        (a2 - c2)+tan(α)(c1 - a1)
r2 = -------------------------------
       tan(α)(d1 - a1) - (d2 - a2)
```
