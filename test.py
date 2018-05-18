import pandas as pd

list1 = [35.8, 19.866666666666667, 98.88333333333334, 118.88333333333334, 72.5, 26.733333333333334, 28.016666666666666, 43.0, 40.81666666666667, 24.333333333333332, 98.28333333333333, 17.733333333333334, 145.36666666666667, 26.25, 55.516666666666666, 32.25, 12.15, 52.03333333333333, 66.8, 119.25, 110.75, 23.783333333333335, 56.38333333333333, 34.21666666666667, 17.183333333333334, 23.516666666666666, 19.083333333333332, 79.38333333333334, 24.066666666666666, 107.55, 18.016666666666666, 208.68333333333334, 26.25, 55.516666666666666, 30.983333333333334, 17.666666666666668, 20.633333333333333, 19.3, 70.76666666666667, 34.21666666666667, 58.916666666666664, 67.13333333333334, 127.56666666666666, 97.51666666666667, 20.3, 56.083333333333336, 11.866666666666667, 21.616666666666667, 22.75, 25.5, 88.51666666666667, 21.133333333333333, 108.11666666666666, 23.45, 196.66666666666666, 23.65, 54.78333333333333, 24.666666666666668, 11.433333333333334, 21.333333333333332, 22.433333333333334, 24.783333333333335, 70.4, 21.25, 104.91666666666667, 17.1, 123.06666666666666, 54.483333333333334, 21.1, 19.966666666666665, 18.133333333333333, 19.4, 17.133333333333333, 70.21666666666667, 29.45, 65.63333333333334, 22.3, 25.4, 55.766666666666666, 20.433333333333334, 18.116666666666667, 17.6, 18.383333333333333, 18.5, 30.933333333333334, 25.366666666666667, 20.616666666666667, 115.85, 26.816666666666666, 22.4, 55.13333333333333, 21.15, 16.2, 16.5, 20.0, 19.65, 24.6, 31.9, 18.533333333333335, 118.38333333333334]
list2 = [22.1, 19.542424242424243, 25.797777777777775, 69.7095238095238, 65.74722222222222, 29.454545454545453, 28.865000000000002, 29.816666666666666, 24.3, 25.460416666666667, 48.951851851851856, 20.31574074074074, 81.71388888888889, 27.597916666666666, 18.938888888888886, 22.747619047619047, 13.182291666666666, 31.72416666666667, 36.5787037037037, 67.5, 36.05, 23.148809523809522, 21.758333333333333, 21.364035087719298, 15.191666666666666, 23.735416666666666, 19.390625, 34.425, 25.460416666666667, 56.377272727272725, 20.31574074074074, 81.71388888888889, 27.597916666666666, 18.938888888888886, 19.061111111111114, 16.307291666666668, 19.673333333333336, 19.725925925925928, 33.0037037037037, 28.85, 51.61833333333333, 22.884210526315787, 66.21904761904763, 33.98125, 20.583333333333332, 21.85, 12.302083333333334, 20.738888888888887, 23.67037037037037, 24.124444444444446, 32.891666666666666, 21.7078431372549, 57.56984126984127, 18.89, 104.60833333333333, 23.78111111111111, 18.783333333333335, 23.345833333333335, 12.36372549019608, 20.738888888888887, 23.67037037037037, 24.124444444444446, 32.891666666666666, 21.7078431372549, 57.56984126984127, 19.369444444444447, 176.26666666666668, 19.303333333333335, 22.55277777777778, 17.923333333333336, 18.642222222222223, 22.226666666666667, 17.293859649122805, 34.73148148148148, 28.183333333333334, 50.47753623188406, 26.510526315789473, 27.52619047619048, 19.47222222222222, 21.895238095238096, 17.814912280701755, 18.211111111111112, 22.706666666666667, 18.38947368421053, 33.327777777777776, 29.183333333333334, 21.09722222222222, 67.5, 32.96875, 23.148809523809522, 21.758333333333333, 21.341666666666665, 16.161458333333332, 17.19722222222222, 22.097058823529412, 20.33076923076923, 28.016666666666666, 49.67037037037037, 20.00294117647059, 80.38333333333334]
list3 = [38.268156424580994, 1.6320927394752895, 73.91089387044218, 41.363081051851566, 9.314176245210732, 10.179097710269772, 3.0279595478881727, 30.65891472868217, 40.465496120865666, 4.6318493150685, 50.1931302168711, 14.562447786131985, 43.78773981502714, 5.1349206349206336, 65.88612028419895, 29.46474713916575, 8.496227709190665, 39.031069827033946, 45.24146152140165, 43.39622641509434, 67.44920993227991, 2.6679347282010357, 61.409991132131246, 37.5624887840644, 11.590688651794377, 0.9301913536498938, 1.6102620087336306, 56.634474070963684, 5.791204986149587, 47.58040657622248, 12.760818172474048, 60.843116896946455, 5.1349206349206336, 65.88612028419895, 38.47946924870001, 7.694575471698113, 4.65266558966073, 2.2068700825177583, 53.362641963678236, 15.68436434486118, 12.387553041018386, 65.9122981236607, 48.09063421553622, 65.15339258246453, 1.3957307060755244, 61.04011887072808, 3.669241573033709, 4.06065278848626, 4.045584045584048, 5.394335511982564, 62.84127282997552, 2.7185006494711437, 46.752112283174405, 19.445628997867797, 46.809322033898304, 0.5543810194972951, 65.71341648919989, 5.354729729729728, 8.137540730577955, 2.7864583333333357, 5.514280997193331, 2.6585967271912123, 53.27888257575758, 2.1545559400230645, 45.12803056091381, 13.271604938271611, 43.22860238353198, 64.57020495564393, 6.885202738283313, 10.233722871452402, 2.8063725490196156, 14.570446735395196, 0.93692402211754, 50.53669857847404, 4.301075268817201, 23.091615695453445, 18.881283927307052, 8.370828646419213, 65.08268579398286, 7.154509438359358, 1.665617585822883, 3.4722222222222197, 23.517679057116958, 0.5974395448079521, 7.740660919540223, 15.045992115637318, 2.330908111021282, 41.73500215796288, 22.941267868241145, 3.342899659863944, 60.53506650544136, 0.9062253743104796, 0.23791152263374782, 4.225589225589208, 10.485294117647062, 3.46447445684088, 13.888888888888879, 55.70649018924881, 7.929538721963601, 32.09911305082359]

df = pd.DataFrame(list2, list1)
df.to_csv("testArray.csv")