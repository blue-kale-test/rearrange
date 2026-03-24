README.md

Rearrange
=========

This module is used for rearranging names.
Turns "LasName, FirstName" into "FirstName Lastname"

## Example

 * Calling 'rearrange_name("Frost, Robert") will return "Robert Frost"
 * Calling `rearrange_name("Hopper, Grace M.")` will return `"Grace M. Hopper"`
 * Calling `rearrange_name("Voltaire")` will return `"Voltaire"`

Fixed the case correction issue.

## Example 

 * Calling `rearrange_name("bond, james")` will return "James Bond"
 * Calling `rearrange_name("KHAnna, raJEsh")` will return "Rajesh Khanna"
