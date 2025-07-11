// QuaggaJS başlatma işlemi
Quagga.init({
    inputStream: {
        name: "Live",
        type: "LiveStream",
        target: document.querySelector('#scanner'),
        constraints: {
            facingMode: "environment"
        }
    },
    decoder: {
        readers: ["ean_reader", "ean_8_reader", "upc_reader", "upc_e_reader"] // EAN-13 için gerekli okuyucuları ekleyin
    }
}, function(err) {
    if (err) {
        console.log(err);
        return;
    }
    console.log("Quagga başlatıldı!");
    Quagga.start();
});

// Barkod okuma işlevi
Quagga.onDetected(function(result) {
    var code = result.codeResult.code;
    console.log("Barkod Okundu:", code);
    document.getElementById('barcode-output').textContent = code; 
});
