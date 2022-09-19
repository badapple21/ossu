(* This is a commet. This is our first program *)


val x = 34;
(* staic enviroment: x : int *)
(* dynamic enviroment: x --> 34 *)

val y = 17;
(* staic enviroment: x : int, y : int *)

(* dynmic enivorment: x --> 34, y -- 17 *)

val z = (x + y) + (y + 2);
(* staic enviroment: x : int, y : int, z : int *)
(* dynmic enivorment: x --> 34, y -- 17, z --> 70 *)

val q = z + 1;
(* staic enviroment: x : int, y : int, z : int, q : int *)
(* dynmic enivorment: x --> 34, y -- 17, z --> 70, w --> 71 *)

val abs_of_z = if z < 0 then 0 - z else z;
(* abs_of_z : int *)
(* dynamic Enivorment: ..., abs_of_z --> 70 *)

val abs_of_z_simpler = abs z;
