#!/bin/bash
rrdtool create p1.rrd \
	-s 10 \
	DS:VerbruikTotaalHoog:GAUGE:20:0:100000 \
	DS:VerbruikTotaalLaag:GAUGE:20:0:100000 \
	DS:LeveringTotaalHoog:GAUGE:20:0:100000 \
	DS:LeveringTotaalLaag:GAUGE:20:0:100000 \
	DS:TariefIndicator:GAUGE:20:0:5 \
	DS:huidigVerbruik:GAUGE:20:0:10000 \
	DS:huidigLeveren:GAUGE:20:0:10000 \
	RRA:AVERAGE:0.5:1:65000 \
	RRA:AVERAGE:0.5:30:8928 \
	RRA:AVERAGE:0.5:180:35136 \
	RRA:AVERAGE:0.5:360:87840 \
	RRA:MIN:0.5:1:65000 \
	RRA:MIN:0.5:30:8928 \
	RRA:MIN:0.5:180:35136 \
        RRA:MIN:0.5:360:87840 \
	RRA:MAX:0.5:1:65000 \
        RRA:MAX:0.5:30:8928 \
        RRA:MAX:0.5:180:35136 \
        RRA:MAX:0.5:360:87840 \
	RRA:LAST:0.5:1:65000 \
	RRA:LAST:0.5:30:8928 \
	RRA:LAST:0.5:180:35136 \
	RRA:LAST:0.5:360:87840 
 