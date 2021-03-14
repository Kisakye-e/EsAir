const cloudinary = require("../config/cloudinary");
const { logObject, logElement, logText } = require("./log");
const {
  axiosError,
  tryCatchErrors,
  missingQueryParams,
  callbackErrors,
} = require("./errors");

const deleteFromCloudinary = (imageID) => {
  try {
    logText(".....deleting image from cloudinary......");
    cloudinary.uploader.destroy(imageID, function(error, result) {
      if (result) {
        logText("we have gotten the result we want");
        return {
          success: true,
          message: "image delete successfully",
        };
      } else if (error) {
        logObject("unable to delete in cloud", error);
        return {
          success: false,
          message: "unable to delete from cloud",
          error: error,
        };
      } else {
        logText("we are not sure tsup in the cloudinary deletion util");
        return {
          success: false,
          message: "we are not sure tsup in the cloudinary deletion util",
        };
      }
    });
  } catch (error) {
    logElement("server error", error.message);
    return {
      success: false,
      message: "server error",
      error: error.message,
    };
  }
};

module.exports = { deleteFromCloudinary };
