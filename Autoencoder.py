"""
Autoencoder model to learn on baseline calcium transients
"""
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

class AutoencoderSimple(Model):
  def __init__(self):
    super(AutoencoderSimple, self).__init__()
    self.encoder = tf.keras.Sequential([
      layers.Dense(400, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(272, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(136, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(72, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(32, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(12, activation="tanh"),
      ])

    self.decoder = tf.keras.Sequential([
      layers.Dense(32, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(72, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(136, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(272, activation="tanh"),
      layers.Dropout(0.2),
      layers.Dense(400, activation="sigmoid")])

  def call(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded

autoencoder = AutoencoderSimple()
autoencoder.compile(optimizer='adam', loss='mse')

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=20, #previously 10
    restore_best_weights=True,
    verbose=1)

lr_schedule = ReduceLROnPlateau( #better than fixed learning rates, better convergence, stable training and fine tunes weights
    monitor='val_loss',factor=0.5, patience=10, min_lr=1e-6,verbose=1)

history = autoencoder.fit(train_data, train_data,
    epochs=500,
    batch_size=64, #previously was 64
    validation_data=(test_data, test_data),
    shuffle=True,
    callbacks=[early_stop, lr_schedule])

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.legend()
plt.show()
