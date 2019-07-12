# 2D Ray tracing tests
My goal is to play around with 2D graphics. The project is completely open so feel free to contribute.

## To Do's
* Map rework.
* Ray bounce and search for light source.
* Rays illuminate area.
* Keyboard control to switch modes.

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
This can be used as a quick check to wether the point actually exists. If the denominator is _0_, the result is an indetermination and the point does not exist. Once _r2_ is computed, it is important to check wether it is positive and less than one. Then, it can be used to compute _r1_ and the actual _X_ point, which are used to plot the ray.
