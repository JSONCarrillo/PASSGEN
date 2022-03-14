package ifneeded Tcldot 2.50.0 "
	load [file join $dir libtcldot.so.0] Tcldot"
package ifneeded Tclpathplan 2.50.0 "
	load [file join $dir libtclplan.so.0] Tclpathplan"
package ifneeded Gdtclft 2.50.0 "
	load [file join $dir libgdtclft.so.0] Gdtclft"
package ifneeded gv 0 "
	load [file join $dir libgv_tcl.so] gv"
# end
