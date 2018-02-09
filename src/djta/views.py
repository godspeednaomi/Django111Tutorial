
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    f_title = '智慧居家燈光控制'
    html_ = f"""
    <!doctype html>
    <html lang="en">
    <head>
    	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1">
    	<title>jQuery UI Slider - Colorpicker</title>
    	<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    	<link rel="stylesheet" href="/resources/demos/style.css">
    	<style>
    	#red, #green, #blue {
    		float: left;
    		clear: left;
    		width: 300px;
    		margin: 15px;
    	}
    	#swatch {
    		width: 120px;
    		height: 100px;
    		margin-top: 18px;
    		margin-left: 350px;
    		background-image: none;
    	}
    	#red .ui-slider-range { background: #ef2929; }
    	#red .ui-slider-handle { border-color: #ef2929; }
    	#green .ui-slider-range { background: #8ae234; }
    	#green .ui-slider-handle { border-color: #8ae234; }
    	#blue .ui-slider-range { background: #729fcf; }
    	#blue .ui-slider-handle { border-color: #729fcf; }
    	</style>
    	<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    	<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    	<script>
    	$( function() {
    		function hexFromRGB(r, g, b) {
    			var hex = [
    				r.toString( 16 ),
    				g.toString( 16 ),
    				b.toString( 16 )
    			];
    			$.each( hex, function( nr, val ) {
    				if ( val.length === 1 ) {
    					hex[ nr ] = "0" + val;
    				}
    			});
    			return hex.join( "" ).toUpperCase();
    		}
    		function refreshSwatch() {
    			var red = $( "#red" ).slider( "value" ),
    				green = $( "#green" ).slider( "value" ),
    				blue = $( "#blue" ).slider( "value" ),
    				hex = hexFromRGB( red, green, blue );
    			$( "#swatch" ).css( "background-color", "#" + hex );
    		}
    		$( "#red, #green, #blue" ).slider({
    			orientation: "horizontal",
    			range: "min",
    			max: 255,
    			value: 127,
    			slide: refreshSwatch,
    			change: refreshSwatch
    		});
    		$( "#red" ).slider( "value", 255 );
    		$( "#green" ).slider( "value", 140 );
    		$( "#blue" ).slider( "value", 60 );
    	} );
    	</script>
    </head>
    <body class="ui-widget-content" style="border:0;">
    <p class="ui-state-default ui-corner-all ui-helper-clearfix" style="padding:4px;">
    	<span class="ui-icon ui-icon-pencil" style="float:left; margin:-2px 5px 0 0;"></span>
    {f_title}
    </p>
    <div id="red"></div>
    <div id="green"></div>
    <div id="blue"></div>
    <!--<div id="swatch" class="ui-widget-content ui-corner-all"></div>-->
    </body>
    </html>
    """
    return HttpResponse(html_)
