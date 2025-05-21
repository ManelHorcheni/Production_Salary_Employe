from prediction import train_dummy_model, encode_inputs

def test_model_prediction():
    model = train_dummy_model("Régression Linéaire")
    data = encode_inputs()
    result = model.predict(data)
    assert result[0] > 0
