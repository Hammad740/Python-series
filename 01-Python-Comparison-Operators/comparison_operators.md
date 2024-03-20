# Comparison Operators

In this we will be learning about Comparison Operators in Python. These operators will allow us to compare variables and output a Boolean value (True or False).

If you have any sort of background in Math, these operators should be very straight forward.

First we'll present a table of the comparison operators and then work through some examples:

<h2> Table of Comparison Operators </h2><p>  In the table below, a=3 and b=4.</p>

<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
</tr>
<tr>
<td>==</td>
<td>If the values of two operands are equal, then the condition becomes true.</td>
<td> (a == b) is not true.</td>
</tr>
<tr>
<td>!=</td>
<td>If values of two operands are not equal, then condition becomes true.</td>
<td>(a != b) is true</td>
</tr>
<tr>
<td>&gt;</td>
<td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
<td> (a &gt; b) is not true.</td>
</tr>
<tr>
<td>&lt;</td>
<td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
<td> (a &lt; b) is true.</td>
</tr>
<tr>
<td>&gt;=</td>
<td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
<td> (a &gt;= b) is not true. </td>
</tr>
<tr>
<td>&lt;=</td>
<td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
<td> (a &lt;= b) is true. </td>
</tr>
</table>

```python
Equal
2 == 2
True
1 == 0
False
Note that == is a comparison operator, while = is an assignment operator.

Not Equal
2 != 1
True
2 != 2
False
Greater Than
2 > 1
True
2 > 4
False
Less Than
2 < 4
True
2 < 1
False
Greater Than or Equal to
2 >= 2
True
2 >= 1
True
Less than or Equal to
2 <= 2
True
2 <= 4
True
```

# Chained Comparison Operators

An interesting feature of Python is the ability to _chain_ multiple comparisons to perform a more complex test. You can use these chained comparisons as shorthand for larger Boolean Expressions.

In this lecture we will learn how to chain comparison operators and we will also introduce two other important statements in Python: **and** and **or**.

Let's look at a few examples of using chains:

```python
1 < 2 < 3
True
```

The above statement checks if 1 was less than 2 **and** if 2 was less than 3. We could have written this using an **and** statement in Python:

```python
1<2 and 2<3
True
```

The **and** is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:

```python
1 < 3 > 2
True
```

The above checks if 3 is larger than both of the other numbers, so you could use **and** to rewrite it as:

```python
1<3 and 3>2
True
```

It's important to note that Python is checking both instances of the comparisons. We can also use **or** to write comparisons in Python. For example:

```python
1==2 or 2<3
True
```

Note how it was true; this is because with the **or** operator, we only need one _or_ the other to be true. Let's see one more example to drive this home:

```python
1==1 or 100==1
True
```
