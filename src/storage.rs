use directories::ProjectDirs;
use serde::{Deserialize, Serialize};
use time::Date;

#[derive(Serialize, Deserialize)]
pub struct Habit {
    pub name: String,
}