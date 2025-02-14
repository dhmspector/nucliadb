// Copyright (C) 2021 Bosutech XXI S.L.
//
// nucliadb is offered under the AGPL v3.0 and as commercial software.
// For commercial licensing, contact us at info@nuclia.com.
//
// AGPL:
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.
//
pub mod cli;
pub mod engines;
pub mod file_vectors;
pub mod plot_writer;
pub mod random_vectors;
pub mod reader;
pub mod stats;
pub mod writer;

pub mod cli_interface {
    pub use super::cli::Args;
    pub use super::file_vectors::*;
    pub use super::plot_writer::*;
    pub use super::random_vectors::*;
    pub use super::{engines, reader, writer};
}

pub trait VectorEngine {
    fn add_batch(&mut self, batch_id: String, keys: Vec<String>, embeddings: Vec<Vec<f32>>);
    fn search(&self, no_results: usize, query: &[f32]);
}

pub trait Logger {
    fn report(&mut self) -> cli::BenchR<()>;
}
