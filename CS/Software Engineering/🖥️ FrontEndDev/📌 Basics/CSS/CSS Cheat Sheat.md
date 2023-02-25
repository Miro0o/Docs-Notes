# CSS Cheat Sheat

[TOC]



## CSS values and units
> 🔗 https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#test_your_skills!


### Rem
In CSS rem stands for “root em”, a unit of measurement that represents the font size of the root element. This means that `1rem` equals the font size of the `html` element, which for most browsers has a default value of 16px. Using rem can help ensure consistency of font size and spacing throughout your UI.

According to the [W3C spec](https://www.w3.org/TR/2013/CR-css3-values-20130730/#font-relative-lengths) the definition for one rem unit is:

> Equal to the computed value of `font-size` on the root element. When specified on the `font-size` property of the root element, the rem units refer to the property’s initial value.

The difference between rem units and em units is that [em units](https://www.sitepoint.com/power-em-units-css/) are relative to the font size of their **own** element, not the **root** element. As such they can cascade and cause unexpected results.


### Ref

[Rem in CSS: Understanding and Using rem Units]: https://www.sitepoint.com/understanding-and-using-rem-units-in-css/

