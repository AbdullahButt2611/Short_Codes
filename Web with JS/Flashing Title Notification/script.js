let showingAlert = false;

const interval = setInterval(()=>{
    document.title = showingAlert ? 'Chat App ':' (1) New Message';
    showingAlert = !showingAlert

},1000);



// To Stop the Interval
// clearInterval(interval)