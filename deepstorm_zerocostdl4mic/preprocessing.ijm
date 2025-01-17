// ----------------------------------------------------------------------------------------------
// This macro projects the intensity values of an image to the [0,1] range. Then it applies a 
// mean normalization using specific mean and standard deviation values. 
// Credits:
// - DeepImageJ team:
// 		- Reference: 
//		"DeepImageJ: A user-friendly plugin to run deep learning models in ImageJ", 
// 		E. Gomez-de-Mariscal, C. Garcia-Lopez-de-Haro, et al., bioRxiv 2019.
// ----------------------------------------------------------------------------------------------

// clip the range of values to the [0,1] range
run("32-bit");
getStatistics(_, _, min, max, _, _);
run("Subtract...", "value=" + min);
diff = max - min + 1e-20
run("Divide...", "value=" + diff);
setMinAndMax(0, 1);

// mean normalization
paramMean = 0.23217396438121796;
paramStd = 0.15450893342494965;
run("Subtract...", "value="+paramMean);
run("Divide...", "value="+paramStd);

// Scaling
run("Scale...", "x=8 y=8 interpolation=None create title=upsampled_input");
