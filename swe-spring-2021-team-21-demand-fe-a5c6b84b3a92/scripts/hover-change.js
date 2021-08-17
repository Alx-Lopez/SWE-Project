const div_rideShare = document.getElementById('rideShare');
const div_medicine = document.getElementById('medicine');
const div_water = document.getElementById('water');
const div_electronics = document.getElementById('electronics');

$(div_rideShare).on({
    'mouseenter': function(){
        changeIconColor(div_rideShare);
    },
    'mouseleave': function(){
        revertIconColor(div_rideShare);
    }
}); // End of div_rideShare event listeners

$(div_medicine).on({
    'mouseenter': function(){
        changeIconColor(div_medicine);
    },
    'mouseleave': function(){
        revertIconColor(div_medicine);
    }
}); // End of div_medicine event listeners

$(div_water).on({
    'mouseenter': function(){
        changeIconColor(div_water);
    },
    'mouseleave': function(){
        revertIconColor(div_water);
    }
}); // End of div_water event listeners

$(div_electronics).on({
    'mouseenter': function(){
        changeIconColor(div_electronics);
    },
    'mouseleave': function(){
        revertIconColor(div_electronics);
    }
}); // End of div_electronics event listeners

// TODO: access colors via css, don't have them hardcoded
function changeIconColor(div) {
    const i_icon = div.children[0];
    i_icon.style.color = '#FF9970';
}
function revertIconColor(div) {
    const i_icon = div.children[0];
    i_icon.style.color = '#FFFFFF';
}
