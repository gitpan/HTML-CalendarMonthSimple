#!/usr/bin/perl

use lib ".";
use HTML::CalendarMonthSimple;
$x = new HTML::CalendarMonthSimple();
print "Content-type: text/html\n\n";
print $x->as_HTML;

