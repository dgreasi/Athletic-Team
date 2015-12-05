$('#change_ps').click(function() {
  window.location='/change_info';
});

$('#visitor').click(function() {
  window.location='/home';
});


$(document).ready(function() {
    $('.ranking-slider').each(function() {
        var stepSlider = this;
        var noUIStepSlider = noUiSlider.create(stepSlider, {
            start: [ 5 ],
            step: 1,
            range: {
                   'min': [  0 ],
                   'max': [ 10 ]
            }

        });
        var $stepSliderValueElement = $(stepSlider).siblings('.ranking-slider-val').eq(0);
        if ($stepSliderValueElement.length) {
            stepSlider.noUiSlider.on('update', function( values, handle ) {
                $stepSliderValueElement.val(values[handle]);
            });
           
            $stepSliderValueElement.on('keyup change', function() {
                var $this = $(this);
                noUIStepSlider.set(+$this.val());
            });
        }
    });
});


function view_text () {
    // Find html elements.
    var textTitle = document.getElementById('my_text_title');
    var textArea = document.getElementById('my_text');
    var div = document.getElementById('view_text');
            
    // Put the text in a variable so we can manipulate it.
    var text_title = textTitle.value;
    var text = textArea.value;

    // Make sure html and php tags are unusable by disabling < and >.
    text = text.replace(/\</gi, "<");
    text = text.replace(/\>/gi, ">");
    
    //change \n with <br> so it can be printed wright
    text = text.replace(/\n/gi, "<br />");

    // Basic BBCodes.
    text = text.replace(/\[b\]/gi, "<b>");
    text = text.replace(/\[\/b\]/gi, "</b>");
            
    text = text.replace(/\[i\]/gi, "<i>");
    text = text.replace(/\[\/i\]/gi, "</i>");
            
    text = text.replace(/\[u\]/gi, "<u>");
    text = text.replace(/\[\/u\]/gi, "</u>");

    // Print the text in the div made for it.
    div.innerHTML = text;
}

//Using buttons B, U, I
//Selected text
function mod_selection (val1,val2) {
    // Get the text area
    var textArea = document.getElementById('my_text');

    //if IExplorer
    if( -1 != navigator.userAgent.indexOf ("MSIE") ) { 
                
        var range = document.selection.createRange();
        var stored_range = range.duplicate();
    
        if(stored_range.length > 0) {
            stored_range.moveToElementText(textArea);
            stored_range.setEndPoint('EndToEnd', range);
            textArea.selectionStart = stored_range.text.length - range.text.length;
            textArea.selectionEnd = textArea.selectionStart + range.text.length;
        }
    }

    
            
    // Do we even have a selection?
    if (typeof(textArea.selectionStart) != "undefined") {
        // Split the text in three pieces - the selection, and what comes before and after.
        var begin = textArea.value.substr(0, textArea.selectionStart);
        var selection = textArea.value.substr(textArea.selectionStart, textArea.selectionEnd - textArea.selectionStart);
        var end = textArea.value.substr(textArea.selectionEnd);
        
        // Insert the tags between the three pieces of text.
        textArea.value = begin + val1 + selection + val2 + end;
    }
}


