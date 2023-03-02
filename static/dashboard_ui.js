const flow_size = document.getElementById("flowing-suggestions");

if (flow_size.offsetWidth < 720) {
    flow_size.style.overflowX = 'scroll';
} else {
    flow_size.style.overflowX = 'hidden';
}